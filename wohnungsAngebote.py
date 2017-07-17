import beautifulsoupHelper
import time
import datetime
import pandas as pd

notAvailable = ""

wohnunstyp_arr = []
kaltmiete_arr = []
nebenkosten_arr = []
kautionOderGenoss_arr = []
anzahl_zimmer_arr = []
flaeche_arr = []
baujahr_arr = []
straßeHausNr_arr = []
plz_arr = []
stadt_arr = []
ortsteil_arr = []
bezirk_arr = []


## drive through all result pages
def scrapeResultPage(url_base_result_page):
    ## get base result page as BS object
    base_result_page_soup = beautifulsoupHelper.configBS(url_base_result_page)

    ## get number of sub pages
    num_pages = beautifulsoupHelper.getNumOfPages(base_result_page_soup)
    print("Anzahl an Ergebnisseiten: " + str(num_pages) + "\n------------------------------------\n")

    ## go through all result pages
    for subPage in range(1, num_pages):
        print(str(subPage) + ". Ergebnisseite scrapen...")
        print("https://www.immobilienscout24.de/Suche/S-T/P-" + str(subPage) + "/Wohnung-Miete/Berlin/Berlin\n")
        ## get each result page as BS object
        result_page_soup = beautifulsoupHelper.configBS(
            "https://www.immobilienscout24.de/Suche/S-T/P-" + str(subPage) + "/Wohnung-Miete/Berlin/Berlin")

        ## get list of all items of the result page (ads)
        ulResultList = result_page_soup.find(id="resultListItems")

        ## find all items of result list excluding th hidden duplicates
        ads = ulResultList.find_all(
            lambda tag: tag.name == 'li' and tag.get('class') == ['result-list__listing'] and tag.get('class') != [
                'result-list__listing--hidden'])

        ## loop through all items of a resultPage and call method to scrape each items detail website
        for index, item in enumerate(ads):
            print(str(index + 1) + ". Item-Seite scrapen...")
            scrapeSubPage(item)


## drive into the detail page
def scrapeSubPage(item):
    ## get item ID
    item_id = item['data-id']
    url_detail_page = "https://www.immobilienscout24.de/expose/" + str(item_id)

    ## init BS
    item_soup = beautifulsoupHelper.configBS(url_detail_page)

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
        kaltmiete = item_soup.find(class_="is24qa-kaltmiete").get_text().split()[0].strip()
    else:
        kaltmiete = notAvailable

    if item_soup.find("dd", {"class": "is24qa-nebenkosten"}):
        dd = item_soup.find("dd", {"class": "is24qa-nebenkosten"})
        span = dd.find("span")
        _ = span.extract()

        try:
            nebenkosten = item_soup.find(class_="is24qa-nebenkosten").get_text().split()[0].strip()
        except IndexError:
            nebenkosten = notAvailable
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
        flaeche = item_soup.find(class_="is24qa-wohnflaeche-ca").get_text().split()[0].strip()
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
            bezirk = temp[temp.find("(") + 1:temp.find(")")]
        except IndexError:
            bezirk = notAvailable
    else:
        plz = notAvailable
        stadt = notAvailable
        ortsteil = notAvailable
        bezirk = notAvailable

    # fill global vars
    global wohnunstyp_arr
    wohnunstyp_arr.append(wohnunstyp)
    global kaltmiete_arr
    kaltmiete_arr.append(kaltmiete)
    global nebenkosten_arr
    nebenkosten_arr.append(nebenkosten)
    global kautionOderGenoss_arr
    kautionOderGenoss_arr.append(kautionOderGenoss)
    global anzahl_zimmer_arr
    anzahl_zimmer_arr.append(anzahl_zimmer)
    global flaeche_arr
    flaeche_arr.append(flaeche)
    global baujahr_arr
    baujahr_arr.append(baujahr)
    global straßeHausNr_arr
    straßeHausNr_arr.append(straßeHausNr)
    global plz_arr
    plz_arr.append(plz)
    global stadt_arr
    stadt_arr.append(stadt)
    global ortsteil_arr
    ortsteil_arr.append(ortsteil)
    global bezirk_arr
    bezirk_arr.append(bezirk)


# use pandas to create dataFrame and export it to xlsx
def generateDataFrame(filename):
    apartments = pd.DataFrame({
        "Wohnunstyp": wohnunstyp_arr
        , "Kaltmiete (in €)": kaltmiete_arr
        , "Nebenkosten (in €)": nebenkosten_arr
        , "KautionOderGenoss": kautionOderGenoss_arr
        , "Anzahl_zimmer": anzahl_zimmer_arr
        , "Flaeche (in m²)": flaeche_arr
        , "Baujahr": baujahr_arr
        , "StraßeHausNr": straßeHausNr_arr
        , "PLZ": plz_arr
        , "Stadt": stadt_arr
        , "Ortsteil": ortsteil_arr
        , "Bezirk": bezirk_arr
    })

    # apartments["warmmiete"] = apartments['kaltmiete (in €)'].str.replace(".", "").str.replace(",", ".").astype(float) + apartments['nebenkosten (in €)'].str.replace(".", "").str.replace(",", ".").astype(float)

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')
    file = str(st) + ' ' + filename + '.xlsx'
    engine = 'xlsxwriter'

    writer = pd.ExcelWriter(file, engine=engine)

    # Convert the dataframe to an XlsxWriter Excel object.
    apartments.to_excel(writer, sheet_name=filename)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
