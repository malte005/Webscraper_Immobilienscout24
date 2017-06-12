from bs4 import BeautifulSoup
import requests

# URLs für Wohnungsanebote
url_wohnung_mieten = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/Berlin/Berlin"
url_wohnung_kaufen = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Berlin/Berlin"
url_wohnung_mieten_archiv = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/archiv/Berlin/Berlin"
url_wohnung_kaufen_archiv = "https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/archiv/Berlin/Berlin"

# URL für WG Angebote
url_wg_zimmer_mieten = "https://www.immobilienscout24.de/Suche/S-T/WG-Zimmer/Berlin/Berlin"

page = requests.get(url_wohnung_mieten)

soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())
