from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

mysrc = requests.get("http://192.168.144.20:80/emplist")
#print(mysrc.text)

#mysrc = urlopen("http://192.168.144.20:80/emplist")  
#print(mysrc)

soup = BeautifulSoup(mysrc.text, "html.parser") 
#print(soup)
tables = soup.find_all("table")
trList = tables[0].find_all("tr")
for idx, i in enumerate(trList):
    if idx == 0: continue
    tds = i.find_all("td")
    print(tds[0].get_text(),end="\t")
    print(tds[1].get_text(),end="\t")
    print(tds[2].get_text(),end="\t")
    print(tds[3].get_text())

# for item in trList:
#     tdList = item.select("td")
#     for td in tdList:
#         print(td.get_text(), end=" ")
#     print()