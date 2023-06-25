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
[عربي readme](https://github.com/rly0nheart/ipmap/blob/master/README_ar.md) •
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
usage: 
    Geolocate IP Address(es) (with an interactive map)
    --------------------------------------------------
    ipmap <ip> --map

    Open Google Earth on the given coordinates
    --------------------------------------------
    ipmap <ip> --earth

    Lookup IP Address(es) (same as map but without an interactive map)
    ------------------------------------------------------------------
    ipmap <ip> --lookup
    

IPMap (IP Mapper) — by Richard Mwewa (https://about.me/rly0nheart)

positional arguments:
  ip                    target ip address

options:
  -h, --help            show this help message and exit
  -e, --earth           Open Google Earth on the location of a given ip
  -l, --lookup          Lookup an ip (like --map, but without an interactive
                        map)
  -m, --map             Geolocate an ip (with an interactive map)
  -o OUTPUT, --output OUTPUT
                        map output name (default ipmap)
  -v, --version         show program's version number and exit

A cross-platform easy-to-use ip geolocation & mapping tool.
```
> Du kan också skicka en fil som innehåller ip-adresser till `ip`, IPMap kommer att bearbeta filen därefter och läsa varje ip rad för rad.
# Översättningar
* [Justin Clark](https://github.com/jclark1913) - Lade till [README_ar.md](https://github.com/rly0nheart/ipmap/blob/master/README_ar,md) för arabisk översättning
> Om du vill översätta projektets README till något språk, eller om du kan förbättra (Google-översatta) översättningarna av de redan befintliga README:erna, öppna gärna en pull-förfrågan med dina översättningar. Jag tar mer än gärna med dem i projektet :).
