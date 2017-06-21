from bs4 import BeautifulSoup
##import pandas as pd
import requests

# URLs für Wohnungsanebote
url_wohnung_mieten_base = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/Berlin/Berlin"
url_wohnung_kaufen = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Berlin/Berlin"
url_wohnung_mieten_archiv = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/archiv/Berlin/Berlin"
url_wohnung_kaufen_archiv = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/archiv/Berlin/Berlin"

# URL für WG Angebote
url_wg_zimmer_mieten = "https://www.immobilienscout24.de/Suche/S-T/WG-Zimmer/Berlin/Berlin"


def num_of_pages(soup):
    return len(soup.find_all("option"))


## soll initBS ersetzen
def configBS(url):
    ## download website
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def scrape_resultPages():
    base_soup = configBS(url_wohnung_mieten_base)
    ## get number of sub pages
    num_pages = num_of_pages(base_soup)
    print(num_pages)

    for subPage in range(1, num_pages):
        soup = configBS("https://www.immobilienscout24.de/Suche/S-T/P-" + str(subPage) + "/Wohnung-Miete/Berlin/Berlin")

        ## get all result items (appartments)
        ulResultList = soup.find(id="resultListItems")

        ## find all items in ul
        inserate = ulResultList.find_all(class_="result-list__listing result-list__listing--xl")

        ## call method
        scrape_itemPage(inserate)


## drive into the detail page of each item
def scrape_itemPage(inserate):
    for item in inserate:
        item_id = item['data-id']
        url_detail_page = "https://www.immobilienscout24.de/expose/" + item_id

        ## download detail website
        item_page = requests.get(url_detail_page)

        ## init BS
        item_soup = BeautifulSoup(item_page.content, "html.parser")

        ##get html parent
        item_html = list(item_soup.children)[2]

        ## drive into body
        body = list(item_html.children)[3]

        ## get Kaltmiete
        kaltmiete = item_soup.find(class_="is24qa-kaltmiete").get_text()
        zimmer = item_soup.find(class_="is24qa-zi").get_text()
        flaeche = item_soup.find(class_="is24qa-flaeche").get_text()
        adresse = item_soup.find(class_="address-block").get_text()
        print(kaltmiete + '  ' + adresse)


scrape_resultPages()
