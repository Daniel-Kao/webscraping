from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    bsObj = BeautifulSoup(html.read(), 'lxml')
    print(bsObj.prettify)
    print(bsObj.nonExistentTag.sometag)
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("It worked!")
