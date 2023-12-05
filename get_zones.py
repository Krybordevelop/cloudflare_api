import requests
from cloudflare_auth_module import headers, cloudflare_api_url


def list_all_zones():
    url = f'{cloudflare_api_url}zones'
    headers
    response = requests.get(url, headers=headers)
    return response.json()

all_zones = list_all_zones()

print("List of All Zones:")
for zone in all_zones['result']:
    print(f"Zone ID: {zone['id']}, Zone Name: {zone['name']}, Status: {zone['status']}")