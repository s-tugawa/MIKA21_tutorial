import requests
from bs4 import BeautifulSoup
import re
import sys
import time

year=int(sys.argv[1])
year=year-2
kensen=sys.argv[2]

#プログラム一覧の URL
url="https://www.ieice.org/ken/program/index.php?instsoc=IEICE-B&tgid=IEICE-"+str(kensen)+"&year="+str(year)+"&region=0&sch1=1&schkey=&pnum=0&psize=2&psort=0&layout=&lang=&term=&pskey=&ps1=1&ps2=1&ps3=1&ps4=1&ps5=1&search_mode="


base=requests.get(url)


soup = BeautifulSoup(base.content, "html.parser")
 
elems=soup.find_all('a')
for i in elems:
    if(i.text =="開催プログラム"):
        url=i.get("href") #開催プログラムを取得

        time.sleep(10) # 負荷をかけないよう1アクセスで10秒スリープ
        r = requests.get(url)

        page = BeautifulSoup(r.content, "html.parser")
 
        elems=page.find_all('td',{"style":"max-width:1000px;"})

        for elem in elems:
            list=[]
            #著者名のリストを取得
            for i in elem.find_all(href=re.compile("AUTHOR")):
                list.append(i.text) 
            print(",".join(list))


    
