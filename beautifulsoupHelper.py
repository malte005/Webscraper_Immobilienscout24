from bs4 import BeautifulSoup
import requests


# returns number of resultpages
def getNumOfPages(soup):
    return len(soup.find_all("option"))


## return BS object
def configBS(url):
    ## download website
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")
