import requests

parameter = {
    "amount" : 50,
    "boolean": "boolean"
}
respone = requests.get("https://opentdb.com/api.php?amount=50&type=boolean",params=parameter)
respone.raise_for_status()
data = respone.json()
print(data)
question_data = data["results"]



