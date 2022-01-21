from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

nutritionix_ID = os.getenv('NUTRITIONIX_ID')
nutritionix_key = os.getenv('NUTRITIONIX_KEY')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": nutritionix_ID,
    "x-app-key": nutritionix_key,
    "Content-Type": "application/json"
}

# NOTE: Change variables to fit user's needs
sex = "female"
weight_kg = 72.6
height_cm = 170.18
age = 30

query = input("What exercise did you do today?: ")

exercise_params = {
    "query": query,
    "gender": sex,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=nutritionix_headers)
exercise_response.raise_for_status()
result = exercise_response.json()

# NOTE: User's will need to set up their own sheety account and workout spreadsheet
sheety_post_url = os.getenv('SHEETY_POST_URL')
sheety_token = os.getenv('SHEETY_TOKEN')

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%X")

sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

for exercise in result['exercises']:
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheety_post = requests.post(url=sheety_post_url, json=sheety_params, headers=sheety_headers)
    sheety_post.raise_for_status()
    print(sheety_post.text)
