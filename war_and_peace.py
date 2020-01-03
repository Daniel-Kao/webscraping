from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getList(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        baseObj = BeautifulSoup(html, 'lxml')
        nameList = baseObj.findAll("span", {"class": "green"})
    except AttributeError as e:
        return None
    return nameList


nameList = getList("http://pythonscraping.com/pages/warandpeace.html")
if nameList == None:
    print("Title could not be found")
else:
    for name in nameList:
        print(name.get_text())
