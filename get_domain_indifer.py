import sys
import requests
from cloudflare_auth_module import headers, cloudflare_api_url


# Get zone details for a specific domain
def get_zone_details(domain):
    url = f'{cloudflare_api_url}zones'
    params = {'name': domain, 'status': 'active'}
    headers
    response = requests.get(url, params=params, headers=headers)
    return response.json()

if len(sys.argv) != 2:
    print("Usage: python script.py <domain>")
    sys.exit(1)

domain_name = sys.argv[1]




zone_info = get_zone_details(domain_name)
if zone_info['success'] and len(zone_info['result']) > 0:
    zone = zone_info['result'][0]
    print(f"Zone ID: {zone['id']}")
    print(f"Zone Name: {zone['name']}")
    print(f"Zone Status: {zone['status']}")
else:
    print(f"Domain not found")