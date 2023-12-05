
import requests

def get_account_info():
    url = f'{base_url}user'

    response = requests.get(url, headers=headers)
    return response.json()

account_info = get_account_info()
print(account_info)