import requests

base_url = "https://api.aviationstack.com/v1"
api_key = "1a53b930589ccc2d36a299b36726373d"

def get_api_info():
    url = f"{base_url}/flights"
    params ={"access_key": api_key}

    try:
        response = requests.get(url=url, params=params)
        response.raise_for_status()

        print(response.status_code)
        print(response.json())

    except requests.exceptions.RequestException as e:
        print("Error:" ,e)

if __name__ == "__main__":
    get_api_info()
