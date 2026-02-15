import requests
from dotenv import load_dotenv
import os

load_dotenv()

base_url = "https://api.aviationstack.com/v1"
API_KEY = os.getenv("API_KEY")

def get_api_info():
    url = f"{base_url}/flights"
    params ={"access_key": API_KEY}

    try:
        response = requests.get(url=url, params=params)
        response.raise_for_status()

        print(response.status_code)
        print(response.json())

    except requests.exceptions.RequestException as e:
        print("Error:" ,e)

if __name__ == "__main__":
    get_api_info()
