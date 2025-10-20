import requests

# GET request
# print("fetching data")
# response = requests.get("https://rickandmortyapi.com/api/character/1")

# print(response.status_code)
# data = response.json()
# print(type(data))
# print(data["name"])
# print(data["location"]["name"])

# POST request
print("posting data")
payload = {
    "title": "Man U their last match",
    "description": "Due to Harry Maguire",
    "userId": 2,
}
try:
    response_2 = requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=payload
    )

    print(f"Status code: {response_2.status_code}")
    print(f"Response: {response_2.json()}")
except requests.exceptions.RequestException as e:
    print(f"HTTP Error: {e}")
