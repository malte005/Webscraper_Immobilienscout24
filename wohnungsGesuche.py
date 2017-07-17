import beautifulsoupHelper
import time
import datetime
import pandas as pd


## drive through all result pages
def scrapeResultPage(url_base_result_page):
    print()


## drive into the detail page
def scrapeSubPage(item):
    print()


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
