import requests
OPEN_TRIVIA_URL = "https://opentdb.com/api.php"
AMOUNT = 10
QUESTION_TYPE = "boolean"

parameters = {
    "amount": AMOUNT,
    "type": QUESTION_TYPE
}
# Call the API
response = requests.get(OPEN_TRIVIA_URL, params=parameters)

# Raise an exception if there's any error
response.raise_for_status()

# Parse the API
data = response.json()
question_data = data["results"]