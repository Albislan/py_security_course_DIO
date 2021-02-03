from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')
temperatura = soup.find("p", class_="-gray-dark-2 -font-18 -bold")
print(temperatura.string)
print(soup.title.string)
# print(soup.prettify()) #imprime todo html