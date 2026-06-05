"""
ETL Weather Pipeline
--------------------
Extracts weather details (temperature, humidity, wind speed) for a given city
using the OpenWeather API, transforms them into a structured format,
and loads the results into a CSV file.
"""

import requests
import pandas as pd
from pathlib import Path

# -----------------------------
# CONFIGURATION
# -----------------------------
API_KEY = "YOUR_API_KEY"   # Replace with your valid OpenWeather API key
CITY = "Chennai"
OUTPUT_FILE = Path("weather_output.csv")

# -----------------------------
# ETL PIPELINE
# -----------------------------
def extract_weather(city: str, api_key: str) -> dict:
    """Extract weather data from OpenWeather API for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception(f"API error: {resp.json().get('message', 'Unknown error')}")

def transform_weather(data: dict) -> pd.DataFrame:
    """Transform JSON response into a pandas DataFrame."""
    row = {
        "city": data["name"],
        "temp_c": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return pd.DataFrame([row])

def load_weather(df: pd.DataFrame, output_file: Path) -> None:
    """Load DataFrame into a CSV file."""
    df.to_csv(output_file, index=False)

# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    try:
        data = extract_weather(CITY, API_KEY)
        df = transform_weather(data)
        load_weather(df, OUTPUT_FILE)

        # Print results neatly
        print("✅ Weather data extracted successfully!\n")
        print(f"City       : {df.loc[0, 'city']}")
        print(f"Temp (°C)  : {df.loc[0, 'temp_c']}")
        print(f"Humidity   : {df.loc[0, 'humidity']}")
        print(f"Wind Speed : {df.loc[0, 'wind_speed']}")

    except Exception as e:
        print("❌ Error:", e)
