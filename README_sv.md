[![Docker Image CI](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml)
[![CodeQL](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml)
![GitHub top language](https://img.shields.io/github/languages/top/rly0nheart/ipmap?logo=github)
![PyPI](https://img.shields.io/pypi/v/ipmap?label=Latest%20Release&logo=pypi)
![PyPI - Status](https://img.shields.io/pypi/status/ipmap?label=Status&logo=pypi)

![English readme](README.md) • ![简体中文 readme](README_zh-CN.md) • ![正體中文 readme](README_zh-TW.md) • ![Lengua española readme](README_es.md) • ![Deutsche readme](README_de,md) • ![Svenska readme](README_sv.md) • ![한국어 readme](README_kr.md) • [Français readme](README_fr.md) • ![हिन्दी readme](README_hi.md) • ![Português readme](README_pt.md) • ![Italian readme](README_it.md)
 • ![Русский readme](README_ru.md) • [Indonesian readme](README_id.md) • ![فارسی readme](README_fa.md) • ![Türkçe readme](README_tr.md) • ![Polskie readme](README_pl.md)

IPMap geolokaliserar en given ip-adress/adresser från en fil, och genererar sedan en [broschyr](https://github.com/leaflet/leaflet) karta som visar platsen för varje ip-adress på den (med rätt argument).

# Funktioner
- [x] Slår upp ip-adresser och returnerar tillhörande information.
- [x] Slår upp en ip-adress och returnerar den associerade informationen och pekar sedan på platsen för ip-adresserna på en genererad broschyrkarta.
- [x] Öppnar Google Earth på de angivna koordinaterna (format: latitud longitud).
- [x] Genererade kartor sparas i `kartor`-katalogen som skapas under körning om den inte finns.
- [x] Använder inte externa beroenden för kartan, använder istället en redan skriven html ![kartmall](ipmap/data/templates/map.html).

# Installation
## PyPI
IPMap kan installeras från PyPI genom att köra följande kommando i terminal/kommandotolken
```
pip install ipmap
```
## GitHub
Eller om du föredrar att installera det från källan kan du köra följande kommando
```
pip install git+https://github.com/rly0nheart/ipmap.git
```
## Bygg från källan
``` Python
# installera poesi
pip install poetry

# klona projektet
git clone https://github.com/rly0nheart/ipmap

# flytta till ipmap-katalogen
cd ipmap

# bygg hjulfilen
poetry build

# installera det inbyggda hjulet (Linux)
pip installera dist/*.whl

# installera inbyggt hjul (Windows)
pip install .\dist\generated-wheel-file-name.whl
```

# Användning
För att se användningen kan du helt enkelt springa
```
ipmap --help
```
Utgången ska se ut som följande
```
användande:
     Geolokalisera IP-adresser (med en interaktiv karta)
     --------------------------------------------------
     ipmap map --ip <ip/file_innehållande_ip_adresser>

     Öppna Google Earth på de angivna koordinaterna
     --------------------------------------------
     ipmap earth --koordinater <latitud> <longitud>

     Slå upp IP-adresser (samma som kartan men utan en interaktiv karta)
     -------------------------------------------------- ----------------
     ipmap lookup --ip <ip/file_innehållande_ip_adresser>

lägen:
     map - skapar en interaktiv karta och stift pekar på platserna för de angivna IP-adresserna på den.
     earth - öppnar google earth på de angivna koordinaterna
     lookup - slår upp informationen om den/de angivna ip-adresserna.
    

IPMap (IP Mapper) — av Richard Mwewa (https://about.me/rly0nheart)

positionsargument:
   {earth,lookup,map} init-läge

alternativ:
   -h, --help visa detta hjälpmeddelande och avsluta
   -i IP, --ip IP en ip-adress eller en fil som innehåller ip-adresser
   -o OUTPUT, --output OUTPUT
                         namn på kartutdata
   -c COORDINATES COORDINATES, --coordinates COORDINATES COORDINATES
                         rymdseparerade latitud och longitud
   -v, --version visar programmets versionsnummer och avsluta

Ett plattformsoberoende lättanvänt verktyg för geolokalisering och kartläggning av IP.
```
