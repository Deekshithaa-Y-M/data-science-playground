from __future__ import annotations

import argparse
import json
import logging
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


@dataclass
class PipelineConfig:
	input_path: Path
	output_csv_path: Path
	output_db_path: Path
	quality_report_path: Path
	table_name: str
	drop_duplicates: bool


def build_parser(default_dir: Path) -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(
		description="Production-style ETL: validate CSV, clean data, save CSV + SQLite + quality report."
	)
	parser.add_argument(
		"--input",
		type=Path,
		default=default_dir / "input.csv",
		help="Path to source CSV file.",
	)
	parser.add_argument(
		"--output-csv",
		type=Path,
		default=default_dir / "cleaned_output.csv",
		help="Path to cleaned output CSV.",
	)
	parser.add_argument(
		"--output-db",
		type=Path,
		default=default_dir / "etl_output.db",
		help="Path to SQLite output database.",
	)
	parser.add_argument(
		"--quality-report",
		type=Path,
		default=default_dir / "data_quality_report.json",
		help="Path to write data quality report JSON.",
	)
	parser.add_argument(
		"--table-name",
		type=str,
		default="clean_table",
		help="Destination SQLite table name.",
	)
	parser.add_argument(
		"--keep-duplicates",
		action="store_true",
		help="Keep duplicate rows (default behavior is to drop duplicates).",
	)
	return parser


def setup_logging() -> None:
	logging.basicConfig(
		level=logging.INFO,
		format="%(asctime)s | %(levelname)s | %(message)s",
	)


def ensure_parent_dir(path: Path) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)


def extract(input_path: Path) -> pd.DataFrame:
	if not input_path.exists():
		raise FileNotFoundError(
			f"Input file not found: {input_path}. Provide a valid CSV path via --input."
		)

	logging.info("Extracting source data from %s", input_path)
	df = pd.read_csv(input_path)
	if df.empty:
		raise ValueError("Input CSV contains no rows.")
	return df


def validate_required_columns(df: pd.DataFrame, required_columns: list[str]) -> None:
	missing = [col for col in required_columns if col not in df.columns]
	if missing:
		raise ValueError(
			"Missing required columns: "
			+ ", ".join(missing)
			+ ". Expected at least: "
			+ ", ".join(required_columns)
		)


def transform(df: pd.DataFrame, drop_duplicates: bool) -> pd.DataFrame:
	required_columns = ["Name", "Age"]
	validate_required_columns(df, required_columns)

	cleaned = df.copy()

	cleaned["Age"] = pd.to_numeric(cleaned["Age"], errors="coerce")
	cleaned["Age"] = cleaned["Age"].fillna(cleaned["Age"].median())

	cleaned["Name"] = cleaned["Name"].fillna("Unknown").astype(str).str.strip()
	cleaned.loc[cleaned["Name"].eq(""), "Name"] = "Unknown"

	if drop_duplicates:
		before = len(cleaned)
		cleaned = cleaned.drop_duplicates()
		dropped = before - len(cleaned)
		logging.info("Dropped %d duplicate rows", dropped)

	cleaned["etl_processed_at"] = pd.Timestamp.utcnow().isoformat()
	return cleaned


def build_quality_report(raw_df: pd.DataFrame, clean_df: pd.DataFrame) -> dict[str, Any]:
	null_counts = clean_df.isnull().sum().to_dict()
	report = {
		"raw_row_count": int(len(raw_df)),
		"clean_row_count": int(len(clean_df)),
		"columns": list(clean_df.columns),
		"null_counts": {k: int(v) for k, v in null_counts.items()},
		"duplicate_rows_after_cleaning": int(clean_df.duplicated().sum()),
		"age_summary": {
			"min": float(clean_df["Age"].min()),
			"max": float(clean_df["Age"].max()),
			"mean": float(clean_df["Age"].mean()),
			"median": float(clean_df["Age"].median()),
		},
	}
	return report


def load_csv(df: pd.DataFrame, output_csv_path: Path) -> None:
	ensure_parent_dir(output_csv_path)
	df.to_csv(output_csv_path, index=False)
	logging.info("Saved cleaned CSV to %s", output_csv_path)


def load_sqlite(df: pd.DataFrame, output_db_path: Path, table_name: str) -> None:
	ensure_parent_dir(output_db_path)
	with sqlite3.connect(output_db_path) as conn:
		df.to_sql(table_name, conn, if_exists="replace", index=False)
	logging.info("Loaded %d rows into %s (%s)", len(df), output_db_path, table_name)


def save_quality_report(report: dict[str, Any], quality_report_path: Path) -> None:
	ensure_parent_dir(quality_report_path)
	quality_report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
	logging.info("Saved data quality report to %s", quality_report_path)


def run_pipeline(config: PipelineConfig) -> None:
	raw_df = extract(config.input_path)
	clean_df = transform(raw_df, drop_duplicates=config.drop_duplicates)
	quality_report = build_quality_report(raw_df, clean_df)

	load_csv(clean_df, config.output_csv_path)
	load_sqlite(clean_df, config.output_db_path, config.table_name)
	save_quality_report(quality_report, config.quality_report_path)

	logging.info("ETL pipeline completed successfully")


def main() -> None:
	setup_logging()
	base_dir = Path(__file__).resolve().parent
	parser = build_parser(base_dir)
	args = parser.parse_args()

	config = PipelineConfig(
		input_path=args.input,
		output_csv_path=args.output_csv,
		output_db_path=args.output_db,
		quality_report_path=args.quality_report,
		table_name=args.table_name,
		drop_duplicates=not args.keep_duplicates,
	)

	run_pipeline(config)


if __name__ == "__main__":
	main()