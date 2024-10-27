import requests

url = "https://booking.airserbia.com/api/graphql"

query = """
{
  flights(origin: "BEG", destination: "MLA", date: "2024-10-27") {
    id
    departureTime
    arrivalTime
    price
    airline
  }
}
"""

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

response = requests.post(url, json={"query": query}, headers=headers)

if response.status_code == 200:
    print("Uspešan zahtev!")
    print("Podaci o letu:", response.json())
else:
    print("Neuspešan zahtev:", response.status_code)
    print("Detalji:", response.text)
