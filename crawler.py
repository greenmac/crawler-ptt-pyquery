import requests
from pyquery import PyQuery as pq

# Application -> cookies 紀錄 {'over18':'1'}
cookies = {'over18' : '1'}
res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies = cookies)

mainPageDoc = pq(res.text) # 利用pq顯示html跟我們一般看到的格式一樣

for i in range(3):
    title_author = mainPageDoc('div.title > a').items() # 為了疊代
    for each in title_author:
        print(each.text(), each.parent().siblings('.meta > .author').text())

    mainPageDoc.make_links_absolute(base_url = res.url) # 把文檔中的路徑改成絕對路徑
    paging = mainPageDoc('div.btn-group.btn-group-paging > a:nth-child(2)').attr('href')
    res = requests.get(paging, cookies = cookies)
    mainPageDoc = pq(res.text)
    # print(pq(res.text))