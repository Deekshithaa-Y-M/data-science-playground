"""Weather ETL pipeline.

This script demonstrates a simple extract-transform-load flow:
1. Extract weather data from OpenWeather.
2. Transform the JSON response into a tidy table.
3. Load the table into a CSV file.

The script is written to be easy to read, easy to run from GitHub, and easy to
explain in an interview.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import pandas as pd
import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"
DEFAULT_CITY = "Chennai"
DEFAULT_OUTPUT_FILE = Path("weather_output.csv")
DEFAULT_TIMEOUT_SECONDS = 10


def extract_weather(city: str, api_key: str) -> dict:
    """Fetch raw weather data for one city from the OpenWeather API."""

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(API_URL, params=params, timeout=DEFAULT_TIMEOUT_SECONDS)

    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        message = response.json().get("message", response.text)
        raise RuntimeError(f"OpenWeather API error: {message}") from exc

    return response.json()


def transform_weather(data: dict) -> pd.DataFrame:
    """Convert the API response into a one-row pandas DataFrame."""

    row = {
        "city": data["name"],
        "temperature_c": data["main"]["temp"],
        "humidity_percent": data["main"]["humidity"],
        "wind_speed_mps": data["wind"]["speed"],
    }

    return pd.DataFrame([row])


def load_weather(df: pd.DataFrame, output_file: Path) -> None:
    """Save the transformed data to a CSV file."""

    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)


def get_api_key() -> str:
    """Read the OpenWeather API key from the environment."""

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing OPENWEATHER_API_KEY environment variable. "
            "Set it before running the script."
        )
    return api_key


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description="Download and save weather data.")
    parser.add_argument("--city", default=DEFAULT_CITY, help="City to fetch weather for")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_FILE,
        help="CSV file to create or overwrite",
    )
    return parser.parse_args()


def print_weather_report(df: pd.DataFrame) -> None:
    """Print a small human-readable summary."""

    record = df.iloc[0]
    print("Weather data extracted successfully.\n")
    print(f"City               : {record['city']}")
    print(f"Temperature (°C)    : {record['temperature_c']}")
    print(f"Humidity (%)        : {record['humidity_percent']}")
    print(f"Wind speed (m/s)    : {record['wind_speed_mps']}")


def main() -> None:
    """Run the ETL pipeline end to end."""

    args = parse_args()
    api_key = get_api_key()

    weather_data = extract_weather(args.city, api_key)
    weather_frame = transform_weather(weather_data)
    load_weather(weather_frame, args.output)
    print_weather_report(weather_frame)
    print(f"CSV saved to: {args.output.resolve()}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}")
