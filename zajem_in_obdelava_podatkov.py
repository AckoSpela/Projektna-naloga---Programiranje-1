import re
import orodja

# url strani s podatki
prehrana_frontpage_url = 'https://www.studentska-prehrana.si/sl/restaurant'
# datoteka s stranjo
frontpage_filename = 'prehrana_stran.html'

vzorec_bloka = re.compile(
    r'<div class="row restaurant.*?(data-naslov.*?<div class="pull-right margin-right-10">.*?)</div>',
    flags=re.DOTALL
)

vzorec_restavracije = re.compile(
    r'data-cena="(?P<cena_obroka>.*?)"\s*?'
    r'data-doplacilo="(?P<doplacilo>.*?)"'
    r'\s*?data-posid="(?P<id>\d{4})".*?'
    r'<a href="/sl/restaurant/Details/\d*?">\s*(?P<ime>.*?)\s*?</a>.*?<small>\s*?<i>'
    r'(?P<naslov>.*,\s\d{4}\s'
    r'(?P<kraj>.*?))</i>',
    flags=re.DOTALL
)

vzorec_lastnosti = re.compile(
    r'alt=".*?"\s*?title="(?P<lastnost>.*?)"',
    flags=re.DOTALL
)


def izlocimo_lastnosti(blok):
    lastnost = vzorec_lastnosti.findall(blok)
    return lastnost

# Izločimo zajete podatke iz bloka za restavracijo
def izlocimo_podatke(blok):
    restavracija = vzorec_restavracije.search(blok).groupdict()
    restavracija['cena_obroka'] = float(restavracija['cena_obroka'].replace(',','.'))
    restavracija['doplacilo'] = float(restavracija['doplacilo'].replace(',','.')) 
    restavracija['id'] = int(restavracija['id'])
    restavracija['lastnosti'] = izlocimo_lastnosti(blok)
    return restavracija

def izlocimo_gnezdene_podatke(restavracije):
    lastnosti = []
    
    for restavracija in restavracije:
        for lastnost in restavracija.pop('lastnosti'):
            lastnosti.append({'restavracija': restavracija['id'], 'lastnost': lastnost})

    lastnosti.sort(key=lambda lastnost: (lastnost['restavracija'], lastnost['lastnost']))

    return lastnosti


# tu sem zaj spremenila finditer v findall

def izlocimo_restavracije_s_strani(url):
    podatki = []
    orodja.shrani_spletno_stran(url, frontpage_filename)
    vsebina = orodja.vsebina_datoteke(frontpage_filename)
    for blok in vzorec_bloka.findall(vsebina):
        podatki.append(izlocimo_podatke(blok))
    return podatki


restavracije = []
for restavracija in izlocimo_restavracije_s_strani(prehrana_frontpage_url):
    restavracije.append(restavracija)

restavracije.sort(key=lambda restavracija: restavracija['id'])
orodja.zapisi_json(restavracije, 'obdelani-podatki/restavracije.json')
lastnosti = izlocimo_gnezdene_podatke(restavracije)
orodja.zapisi_csv(
    restavracije,
    ['id', 'ime', 'naslov', 'kraj', 'cena_obroka', 'doplacilo'], 'obdelani-podatki/restavracije.csv'
)
orodja.zapisi_csv(lastnosti, ['restavracija', 'lastnost'], 'obdelani-podatki/lastnosti.csv')

vsebina = orodja.vsebina_datoteke(frontpage_filename)


# vsebina = orodja.vsebina_datoteke(frontpage_filename)
# for blok in vzorec_bloka.findall(vsebina):
#     if vzorec_restavracije.search(blok) == None:
#         print(blok)