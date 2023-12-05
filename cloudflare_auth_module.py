from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('API_KEY')
email = os.getenv('EMAIL')

cloudflare_api_url = 'https://api.cloudflare.com/client/v4/'

headers = {
        'X-Auth-Email': email,
        'X-Auth-Key': api_key,
        'Content-Type': 'application/json',
}
