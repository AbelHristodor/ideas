import requests
from bs4 import BeautifulSoup

try:
    CAPITOLO = input(
        "Scegli un capitolo. Usa i numeri romani.\n")
except:
    print("C'è stato un errore. Errore di scrittura?")
URL = f"https://promessisposi.weebly.com/capitolo-{CAPITOLO}.html"
RESP = requests.get(URL)
SOUP = BeautifulSoup(RESP.text, 'lxml')

## ----------------------------TITOLETTI------------------------------------------
TITOLI = SOUP.select("h2")

print("\n\n\n\nEcco i titoletti:\n")

#Eliminiamo ciò che non serve
del TITOLI[-1]
del TITOLI[0]
del TITOLI[-1]
del TITOLI[-1]

C = 0
# Si stampa ogni titoletto numerandolo.
for TITOLO in TITOLI:
    TEXT = TITOLO.get_text()
    C += 1
    print(str(C) + '.' + TEXT)




##  ----------------------------Si passa ai Paragrafi-------------------------------
PARAGRAFI = SOUP.select(".paragraph")

dict = {}
c = 0
# Si prende il testo di ogni paragrafo
for paragrafo in PARAGRAFI: 
    testo = paragrafo.get_text()
    dict.update({c:testo})
    c +=1
# Si elimina cò che non ci interessa
for i in range(1,7):
    del dict[c-i]
del dict[0]
del dict[1]
del dict[2]






