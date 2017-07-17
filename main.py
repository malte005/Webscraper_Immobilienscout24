import wohnungsAngebote as wA

# import wohnungsGesuche as wG

# global variables
immo = "ImmoScout24"
wg = "WG-Gesucht"

# base urls ImmobilienScout24 for offers
url_wohnung_mieten = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/Berlin/Berlin"

# base urls WG-Gesucht for appartment demands
url_wgGesucht_wohnungsGesuche = "www.wg-gesucht.de/wohnungen-in-Berlin-gesucht.8.2.1.0.html"

# Scrape ImmobilienScout24 for offers
wA.scrapeResultPage(url_wohnung_mieten)
wA.generateDataFrame(immo)

# Scrape WG-Gesucht for demands
# wG.scrapeResultPage(url_wgGesucht_wohnungsGesuche)
# wG.generateDataFrame(wg)
