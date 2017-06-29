import wohnungMieten

## base urls
url_wohnung_mieten = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/Berlin/Berlin"
url_wohnung_kaufen = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Berlin/Berlin"
url_wohnung_mieten_archiv = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/archiv/Berlin/Berlin"
url_wohnung_kaufen_archiv = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/archiv/Berlin/Berlin"


# url for shared flat offers
url_wg_zimmer_mieten = "https://www.immobilienscout24.de/Suche/S-T/WG-Zimmer/Berlin/Berlin"


wohnungMieten.scrapeResultPage(url_wohnung_mieten)

