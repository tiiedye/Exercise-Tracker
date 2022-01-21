from dotenv import load_dotenv
import os
import requests

load_dotenv()

nutritionix_ID = os.getenv('NUTRITIONIX_ID')
nutritionix_key = os.getenv('NUTRITIONIX_KEY')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
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

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
exercise_response.raise_for_status()
result = exercise_response.json()
print(result)
