from bs4 import BeautifulSoup
import requests
from datetime import datetime
from day12.daoStock import DaoStock

ds = DaoStock()

ymd_hm = datetime.now().strftime("%Y%m%d_%H%M")
mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding='euc-kr'
soup = BeautifulSoup(mysrc.text, "html.parser") 

mySt = soup.select(".st2")
for idx, item in enumerate(mySt):
    myParent = item.parent
    tds = myParent.select("td")
    s_code = tds[0].a['title']
    s_name = tds[0].text
    price = tds[1].text.replace(',','')
    cnt = ds.insertStock(s_code, s_name, price, ymd_hm)
    print(idx, s_code, s_name, price, ymd_hm, cnt)