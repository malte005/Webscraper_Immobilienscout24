import requests
from bs4 import BeautifulSoup


def getNumOfPages(soup):
    return len(soup.find_all("option"))


## return BS object
def configBS(url):
    ## download website
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


## drive through all result pages
def scrapeResultPage(url_base_result_page):
    ## get base result page as BS object
    base_result_page_soup = configBS(url_base_result_page)

    ## get number of sub pages
    num_pages = getNumOfPages(base_result_page_soup)
    print("Anzahl an Ergebnisseiten: " + str(num_pages) + "\n------------------------------------\n")

    ## go through all result pages
    for subPage in range(1, num_pages):
        print(str(subPage) + ". Ergebnisseite scrapen...")
        print("https://www.immobilienscout24.de/Suche/S-T/P-" + str(subPage) + "/Wohnung-Miete/Berlin/Berlin\n")
        ## get each result page as BS object
        result_page_soup = configBS(
            "https://www.immobilienscout24.de/Suche/S-T/P-" + str(subPage) + "/Wohnung-Miete/Berlin/Berlin")

        ## get list of all items of the result page (ads)
        ulResultList = result_page_soup.find(id="resultListItems")

        ## find all items of result list
        ads = ulResultList.find_all(class_="result-list__listing result-list__listing--xl")

        ## loop through all items of a resultPage and call method to scrape each items detail website
        for index, item in enumerate(ads):
            print(str(index + 1) + ". Item-Seite scrapen...")
            scrapeSubPage(item)


## drive into the detail page
def scrapeSubPage(item):
    notAvailable = "n.a."
    ## get item ID
    item_id = item['data-id']
    url_detail_page = "https://www.immobilienscout24.de/expose/" + str(item_id)

    ## init BS
    item_soup = configBS(url_detail_page)

    ##get html parent
    item_html = list(item_soup.children)[2]
    ##print(item_html)

    ## drive into body
    body = list(item_html.children)[3]
    ##print(body)

    if item_soup.find("dd", {"class": "is24qa-wohnungstyp"}):
        wohnunstyp = item_soup.find(class_="is24qa-wohnungstyp").get_text().strip()
    else:
        wohnunstyp = notAvailable

    if item_soup.find("dd", {"class": "is24qa-kaltmiete"}):
        kaltmiete = item_soup.find(class_="is24qa-kaltmiete").get_text().strip()
    else:
        kaltmiete = notAvailable

    if item_soup.find("dd", {"class": "is24qa-nebenkosten"}):
        nebenkosten = item_soup.find(class_="is24qa-nebenkosten").get_text().strip()
    else:
        nebenkosten = notAvailable

    if item_soup.find("dd", {"class": "is24qa-kaution-o-genossenschaftsanteile"}):
        kautionOderGenoss = item_soup.find(class_="is24qa-kaution-o-genossenschaftsanteile").get_text().strip()
    else:
        kautionOderGenoss = notAvailable

    if item_soup.find("dd", {"class": "is24qa-zimmer"}):
        anzahl_zimmer = item_soup.find(class_="is24qa-zimmer").get_text().strip()
    else:
        anzahl_zimmer = notAvailable

    if item_soup.find("dd", {"class": "is24qa-wohnflaeche-ca"}):
        flaeche = item_soup.find(class_="is24qa-wohnflaeche-ca").get_text().strip()
    else:
        flaeche = notAvailable

    if item_soup.find("dd", {"class": "is24qa-baujahr"}):
        baujahr = item_soup.find(class_="is24qa-baujahr").get_text().strip()
    else:
        baujahr = notAvailable

    if item_soup.find("span", {"class": "block font-nowrap print-hide"}):
        straßeHausNr = item_soup.find(class_="block font-nowrap print-hide").get_text().split(",")[0].strip()
    else:
        straßeHausNr = notAvailable

    if item_soup.find("span", {"class": "zip-region-and-country"}):
        plz = item_soup.find(class_="zip-region-and-country").get_text().split()[0].strip()
        stadt = item_soup.find(class_="zip-region-and-country").get_text().split()[1].split(",")[0].strip()
        try:
            ortsteil = item_soup.find(class_="zip-region-and-country").get_text().split(",")[1].split(" (")[0].strip()
        except IndexError:
            ortsteil = notAvailable
        try:
            temp = item_soup.find(class_="zip-region-and-country").get_text().strip()
            bezirk = temp[temp.find("(")+1:temp.find(")")]
        except IndexError:
            bezirk = notAvailable
    else:
        plz = notAvailable
        stadt = notAvailable
        ortsteil = notAvailable
        bezirk = notAvailable

    print("\t" + wohnunstyp)
    print("\t" + kaltmiete)
    print("\t" + nebenkosten)
    print("\t" + kautionOderGenoss)
    print("\t" + anzahl_zimmer)
    print("\t" + flaeche)
    print("\t" + baujahr)
    print("\t" + straßeHausNr)
    print("\t" + plz)
    print("\t" + stadt)
    print("\t" + ortsteil)
    print("\t" + bezirk)
