# src/yhmt/wikipedia.py
import requests


API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"



def random_page(random_api_url = API_URL):
    try:
        with requests.get(random_api_url) as response:
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as error:
        message = str(error)
        raise click.exceptions.ClickException(message)