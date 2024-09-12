import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY') 
address = '1615+N+Mango+Ave'
key = API_KEY
url = f"https://geocode.search.hereapi.com/v1/geocode?q={address}&apiKey={key}"

response = requests.get(url).json()
# test = response[0]
print(response)