import requests
from bs4 import BeautifulSoup as bs

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = bs(r.text, "html.parser")
data = s.find_all("div", class_="maincounter-number")

print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())
