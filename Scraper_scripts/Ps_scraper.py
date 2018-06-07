'''
Questo è uno semplice script che ricava i titoletti dal sito https://promessisposi.weebly.com
dei capitoli dei promessi sposi. Il capitolo è a scelta dell'utente

'''
import requests
from bs4 import BeautifulSoup

try:
    CAPITOLO = input("Di quale capitolo vuoi sapere i titoletti? Usa i numeri romani.\n")
except:
    print("C'è stato un errore. Errore di scrittura?")
URL = f"https://promessisposi.weebly.com/capitolo-{CAPITOLO}.html"
RESP = requests.get(URL)
SOUP = BeautifulSoup(RESP.text, 'lxml')

# Selezioniamo i titoletti h2

TITOLI = SOUP.select("h2")

print("\n\n\n\nEcco i titoletti:\n")

#Eliminiamo ciò che non serve
del TITOLI[-1]
del TITOLI[0]
del TITOLI[-1]

C = 0
# Si stampa ogni titoletto numerandolo.
for TITOLO in TITOLI:
    TEXT = TITOLO.get_text()
    C += 1
    print(str(C) + '.' + TEXT)
