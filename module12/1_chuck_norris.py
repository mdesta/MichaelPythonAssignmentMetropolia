import json
import urllib.request


def fetch_joke() -> str:
    url = "https://api.chucknorris.io/jokes/random"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; ChuckNorrisJokeFetcher/1.0)"},
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.load(response)
    return data["value"]


def main() -> None:
    try:
        joke = fetch_joke()
        print(joke)
    except Exception as exc:
        print(f"Error fetching joke: {exc}")


if __name__ == "__main__":
    main()
