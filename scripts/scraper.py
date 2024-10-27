import requests
from bs4 import BeautifulSoup

url = "https://www.airserbia.com/sr_latin_RS"

response = requests.get(url)

if response.status_code == 200:
    print("Stranica uspešno preuzeta.")
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Naslov stranice:", soup.title.string)
else:
    print("Greška prilikom preuzimanja: ", response.status_code)

element = soup.find("div")