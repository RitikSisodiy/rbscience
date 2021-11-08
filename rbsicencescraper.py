from requests_html import HTMLSession
import pandas as pd
import requests
session = HTMLSession()
import os
url = "http://rbscience.co.in/archives/"
r= session.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.html.html, 'html.parser')
maindiv = soup.select('div.col-md-9.borderDiv')
mainurl = maindiv[0].select('a')
urlslist = [data.get('href') for data in mainurl]
articals = []
count = 0
print("total urls :" , len(urlslist))
for data in urlslist:
    count += 1
    childcount = 0
    temp = {}
    d= data
    d = d[d.find('?')+1:] 
    d = d.split('&')
    tempdata = {info.split("=")[0]:info.split('=')[1] for info in d }
    temp['year'] = tempdata['y']
    temp['issue'] = tempdata['i'].replace('issue-','')
    temp['vol'] = tempdata['volume'].replace('vol-','')
    d = session.get(data)
    maindiv = d.html.find("div.content-data.current-page")[0]
    links = maindiv.find("p a")
    links = [ li.element.get('href') for li in links ]
    for link in links:
        childcount +=1
        print(f"total {childcount} of {len(links)} of ({count} of {len(urlslist)}) ")
        res = {}
        res.update(temp)
        d = session.get(link)
        res["heading"] = d.html.find('div.row.content div.col-sm-9 h3')[0].text
        contentcontainers = d.html.find('div.row.content div.col-sm-9 div.col-sm-8 div')
        res['authors'] = contentcontainers[0].html
        res['doi'] = contentcontainers[1].html
        res['abstract'] = contentcontainers[2].html
        res['keywords'] = contentcontainers[3].html
        res['references'] = contentcontainers[4].html
        res['pdf'] = d.html.find('div.row.content div.col-sm-9 div.col-sm-4 div.abstract-actions p')[2].find('a')[0].element.get('href')
        pdfname = 'pdf/'+res['pdf'][res['pdf'].rfind('/')+1:]
        if os.path.isfile(pdfname) == False:
            with open(pdfname,'wb') as file:
                filedata = requests.get(res['pdf'])
                file.write(filedata.content)
        res['pdfinlocal'] = pdfname
        articals.append(res)
df = pd.DataFrame(articals)
df.to_csv('scraprbscience.csv' ,index=False)