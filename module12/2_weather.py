import json
import os
import urllib.parse
import urllib.request


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def fetch_weather(city: str, api_key: str) -> tuple[str, float]:
    params = urllib.parse.urlencode({"q": city, "appid": api_key})
    url = f"https://api.openweathermap.org/data/2.5/weather?{params}"

    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.load(response)

    description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    return description, kelvin_to_celsius(float(temp_kelvin))


def main() -> None:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Missing API key. Set environment variable OPENWEATHER_API_KEY.")
        return

    city = input("Enter municipality name: ").strip()
    if not city:
        print("No city provided.")
        return

    try:
        description, temp_c = fetch_weather(city, api_key)
        print(f"Weather: {description}")
        print(f"Temperature: {temp_c:.1f} °C")
    except Exception as exc:
        print(f"Error fetching weather: {exc}")


if __name__ == "__main__":
    main()
