import sys
import os
from pathlib import Path
import pandas as pd


def main(data_dir: Path, outputs_dir: Path):
	data_dir = data_dir.resolve()

	orders_path = data_dir / "orders.csv"
	products_path = data_dir / "products.csv"
	outputs_dir = outputs_dir.resolve()
	outputs_dir.mkdir(parents=True, exist_ok=True)
	out_path = outputs_dir / "orders_enriched.csv"

	missing = [p.name for p in (orders_path, products_path) if not p.exists()]
	if missing:
		print(f"Missing input files in {data_dir}: {', '.join(missing)}")
		print("Place the required CSV files in the data folder and try again.")
		print(f"Files present: {', '.join(p.name for p in data_dir.glob('*'))}")
		sys.exit(1)

	orders = pd.read_csv(orders_path)
	products = pd.read_csv(products_path)
	missing_order_columns = [column for column in ("product_id",) if column not in orders]
	missing_product_columns = [
		column for column in ("product_id", "name", "price") if column not in products
	]
	if missing_order_columns or missing_product_columns:
		raise ValueError(
			"Invalid input schema. "
			f"Missing order columns: {missing_order_columns}; "
			f"missing product columns: {missing_product_columns}"
		)

	print("Orders rows:", len(orders))
	print("Products rows:", len(products))

	# Left join to bring product name/price into orders
	df = orders.merge(products, on="product_id", how="left")

	# Ensure numeric types for qty and price
	if "qty" not in df:
		df["qty"] = 1
	df["qty"] = pd.to_numeric(df["qty"], errors="coerce").fillna(1)
	df["price"] = pd.to_numeric(df.get("price"), errors="coerce")

	# Remove rows with unknown products (missing name or price)
	df = df.dropna(subset=["name", "price"]) 

	# Compute total_price
	df["total_price"] = df["qty"] * df["price"]

	print("\nAfter cleaning rows:", len(df))
	print(df.head())

	df.to_csv(out_path, index=False)
	print(f"\nSaved {out_path}")


if __name__ == "__main__":
	# Try to locate a sibling `data/` directory. When running in notebooks, __file__ may not exist.
	try:
		base = Path(__file__).parent
	except NameError:
		base = Path.cwd()

	def find_ancestor_dir(start: Path, name: str) -> Path | None:
		for p in (start, *start.parents):
			if p.name == name:
				return p
		return None

	# If this script (or its parents) contains a `Data-Engineering` folder,
	# use that folder's `data/` and `outputs/` as the shared locations.
	de_dir = find_ancestor_dir(base, "Data-Engineering")
	if de_dir:
		default_data_dir = de_dir / "data"
		default_outputs_dir = de_dir / "outputs"
	else:
		default_data_dir = base / "data"
		default_outputs_dir = base / "outputs"

	# Allow an environment variable to force a single shared outputs folder
	env_out = os.environ.get("PROJECT_OUTPUTS_DIR")
	if env_out:
		default_outputs_dir = Path(env_out)

	# Allow passing a custom data directory as first argument
	# and an optional outputs directory as second argument
	if len(sys.argv) > 1:
		data_dir = Path(sys.argv[1])
	else:
		data_dir = default_data_dir

	if len(sys.argv) > 2:
		outputs_dir = Path(sys.argv[2])
	else:
		outputs_dir = default_outputs_dir

	main(data_dir, outputs_dir)
