import requests
from bs4 import BeautifulSoup
import json 

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

datos = []

for quote in quotes:
    texto = quote.find("span", class_="text").text
    autor = quote.find("small", class_="author").text
    datos.append({"autor": autor, "cita": texto})

with open("citas json", "w", encoding="utf-8") as archivo_json:
    json.dump(datos, archivo_json, ensure_ascii=False, indent=2)
    

print("archivo de citas guardado correctamente.")



