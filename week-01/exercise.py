import requests

API_KEY = "eXPhuz5EltCCZCd8fY6Wy5Vw1jD2ShpIiDyIJGOY"


def neow(start_date: str, end_date: str):
    response = requests.get(
        "https://api.nasa.gov/neo/rest/v1/feed",
        params={"start_date": start_date, "end_date": end_date, "api_key": API_KEY},
        timeout=8000,
    )
    print(f"Url: {response.url}")
    print(f"Status code: {response.status_code}")
    data = response.json()
    total_neo = data["element_count"]
    neo = data["near_earth_objects"].items()
    result = []
    for date, near_earth_object in neo:  # looping over dates
        for j in near_earth_object:  # looping over neo in date
            result.append(
                {
                    "id": j["id"],
                    "name": j["name"],
                    "is_hazardous": j["is_potentially_hazardous_asteroid"],
                    "date": date,
                }
            )

    return total_neo, result


if __name__ == "__main__":
    start_date = "2025-10-17"
    end_date = "2025-10-20"
    total_neo, result = neow(start_date, end_date)
    print(f"Within {start_date} and {end_date}:")
    print(f"There have been: {total_neo} NEOWs")
    for r in result:
        print("----------------")
        print(f"ID: {r['id']}")
        print(f"Name: {r['name']}")
        print(f"Date: {r['date']}")
        print(f"Is Hazardous: {r['is_hazardous']}")
