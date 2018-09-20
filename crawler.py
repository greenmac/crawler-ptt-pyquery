import requests
from pyquery import PyQuery as pq

dataSet = []
def dataPtt(url, pages=3):
    # Application -> cookies 紀錄 {'over18':'1'}
    cookies = {'over18' : '1'}
    res = requests.get(url, cookies = cookies)
    mainPageDoc = pq(res.text) # 利用pq顯示html跟我們一般看到的格式一樣
    for i in range(pages):
        title_author = mainPageDoc('div.title > a').items() # 為了疊代
        for each in title_author:
            dictDoc = {}
            dictDoc['title'] = each.text()
            dictDoc['author'] = each.parent().siblings('.meta > .author').text()
            dataSet.append(dictDoc)
            # print(each.text(), each.parent().siblings('.meta > .author').text())
        mainPageDoc.make_links_absolute(base_url = res.url) # 把文檔中的路徑改成絕對路徑
        paging = mainPageDoc('div.btn-group.btn-group-paging > a:nth-child(2)').attr('href')
        res = requests.get(paging, cookies = cookies)
        mainPageDoc = pq(res.text)
        # print(pq(res.text))

dataPtt('https://www.ptt.cc/bbs/Gossiping/index.html', 3)
for eachTitleAuthor in dataSet:
    print(eachTitleAuthor)