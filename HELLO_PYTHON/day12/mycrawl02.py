from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

mysrc = requests.get("http://192.168.144.20:80/emplist")
#print(mysrc.text)

#mysrc = urlopen("http://192.168.144.20:80/emplist")  
#print(mysrc)

soup = BeautifulSoup(mysrc.text, "html.parser") 
#print(soup)
tables = soup.select("table")
trList = tables[0].select("tr")
for idx, i in enumerate(trList):
    if idx == 0: continue
    tds = i.select("td")
    print(tds[0].text,end="\t")
    print(tds[1].text,end="\t")
    print(tds[2].text,end="\t")
    print(tds[3].text)
