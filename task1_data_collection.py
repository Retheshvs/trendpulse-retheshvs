import requests
import json

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"  # Free dummy API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open("data_raw.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data fetched and saved!")
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    fetch_data()