
import requests 
from bs4 import BeautifulSoup 
response=requests.get("https://www.google.com/")
soup=BeautifulSoup(response.text,"html.parser")
print(soup.prettify())