[![Docker Image CI](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml)
[![CodeQL](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml)
![GitHub top language](https://img.shields.io/github/languages/top/rly0nheart/ipmap?logo=github)
![PyPI](https://img.shields.io/pypi/v/ipmap?label=Latest%20Release&logo=pypi)
![PyPI - Status](https://img.shields.io/pypi/status/ipmap?label=Status&logo=pypi)

[English readme](https://github.com/rly0nheart/ipmap/blob/master/README.md) • 
[简体中文 readme](https://github.com/rly0nheart/ipmap/blob/master/README_zh-CN.md) • 
[正體中文 readme](https://github.com/rly0nheart/ipmap/blob/master/README_zh-TW.md) • 
[Lengua española readme](https://github.com/rly0nheart/ipmap/blob/master/README_es.md) • 
[Deutsche readme](https://github.com/rly0nheart/ipmap/blob/master/README_de.md) • 
[Svenska readme](https://github.com/rly0nheart/ipmap/blob/master/README_sv.md) • 
[한국어 readme](https://github.com/rly0nheart/ipmap/blob/master/README_kr.md) • 
[Français readme](https://github.com/rly0nheart/ipmap/blob/master/README_fr.md) • 
[हिन्दी readme](https://github.com/rly0nheart/ipmap/blob/master/README_hi.md) • 
[Português readme](https://github.com/rly0nheart/ipmap/blob/master/README_pt.md) • 
[Italian readme](https://github.com/rly0nheart/ipmap/blob/master/README_it.md) • 
[Русский readme](https://github.com/rly0nheart/ipmap/blob/master/README_ru.md) • 
[Indonesian readme](https://github.com/rly0nheart/ipmap/blob/master/README_id.md) • 
[فارسی readme](https://github.com/rly0nheart/ipmap/blob/master/README_fa.md) • 
[Türkçe readme](https://github.com/rly0nheart/ipmap/blob/master/README_tr.md) • 
[Polskie readme](https://github.com/rly0nheart/ipmap/blob/master/README_pl.md)

IPMap geolokaliserar en given ip-adress/adresser från en fil, och genererar sedan en [broschyr karta](https://github.com/leaflet/leaflet) som visar platsen för varje ip-adress på den (med rätt argument).

# Funktioner
* Slår upp ip-adresser och returnerar tillhörande information.
* Slår upp en ip-adress och returnerar den associerade informationen och pekar sedan på platsen för ip-adresserna på en genererad broschyrkarta.
* Öppnar Google Earth på platsen för de angivna IP-adresserna.
* Genererade kartor sparas i "kartor"-katalogen i användarens hemkatalog som skapas under körning om den inte finns.
* Använder inte externa beroenden för kartan, använder istället en redan skriven html [kartmall](ipmap/data/templates/map.html).

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
git-klon https://github.com/rly0nheart/ipmap

# flytta till ipmap-katalogen
cd ipmap

# bygg hjulfilen
poetry build

# installera det inbyggda hjulet (Linux)
pip install dist/*.whl

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
     ipmap map --ip <ip>

     Öppna Google Earth på de angivna koordinaterna
     --------------------------------------------
     ipmap earht --ip <ip>

     Slå upp IP-adresser (samma som kartan men utan en interaktiv karta)
     -------------------------------------------------- ----------------
     ipmap lookup --ip <ip>

lägen:
     map - skapar en interaktiv karta och stift pekar på platserna för de angivna IP-adresserna på den.
     earth - öppnar google earth på platsen för den angivna ip-adressen.
     lookup - slår upp informationen om den/de angivna ip-adresserna.
    

IPMap (IP Mapper) — av Richard Mwewa (https://about.me/rly0nheart)

positionsargument:
   {earth,lookup,map} init-läge

alternativ:
   -h, --help visa detta hjälpmeddelande och avsluta
   -i IP, --ip IP ip
   -o OUTPUT, --output OUTPUT
                         map output namn (standard ipmap)
   -v, --version visar programmets versionsnummer och avsluta

Ett plattformsoberoende lättanvänt verktyg för geolokalisering och kartläggning av IP.
```
> Du kan också skicka en fil som innehåller ip-adresser till `--ip`, IPMap kommer att bearbeta filen därefter och läsa varje ip rad för rad.
# Översättningar
* [Justin Clark](https://github.com/jclark1913) - Lade till [README_ar.md](https://github.com/rly0nheart/ipmap/blob/master/README_ar,md) för arabisk översättning
> Om du vill översätta projektets README till något språk, eller om du kan förbättra (Google-översatta) översättningarna av de redan befintliga README:erna, öppna gärna en pull-förfrågan med dina översättningar. Jag tar mer än gärna med dem i projektet :).
