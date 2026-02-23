import requests

def get_carbon_intensity():
    url = "https://api.carbonintensity.org.uk/intensity"
    response = requests.get(url)
    data = response.json()
    return data["data"][0]["intensity"]["actual"]


def is_carbon_high(threshold=70):
    intensity = get_carbon_intensity()
    return intensity > threshold
