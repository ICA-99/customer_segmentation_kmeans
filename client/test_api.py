import requests

url = "http://127.0.0.1:8000/predict"

age = float(input("Enter your age: "))
income = float(input("Enter your income: "))
spending = float(input("Enter spending hour: "))

payload = {
    "age": age,
    "income": income,
    "spending": spending
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())