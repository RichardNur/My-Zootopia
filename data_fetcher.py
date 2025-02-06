import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
headers = {"X-Api-Key": API_KEY}
URL = "https://api.api-ninjas.com/v1/animals"

def load_data(animal):
    """
    Loads data from API Ninjas for an input animal.

    :params: Loads the data from API Ninjas (url).
    :return: data as list of dictionaries.
    """


    specification = "?name=" + animal
    animal_url = URL + specification

    try:
        res = requests.get(animal_url, headers=headers)
        return res.json()

    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Try again later."}
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}