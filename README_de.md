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

IPMap lokalisiert eine oder mehrere bestimmte IP-Adressen aus einer Datei und generiert dann eine [Leaflet Karte](https://github.com/leaflet/leaflet). Die den Standort jeder darauf befindlichen IP-Adresse genau angibt (mit dem richtigen Argument).

# Merkmale
* Sucht nach IP-Adresse(n) und gibt die zugehörigen Informationen zurück.
* Sucht nach einer oder mehreren IP-Adressen und gibt die zugehörigen Informationen zurück. Anschließend wird der Standort der IP-Adresse(n) auf einer generierten Prospektkarte lokalisiert.
* Öffnet Google Earth am Standort der angegebenen IP-Adresse(n).
* Generierte Karten werden im Verzeichnis „maps“ im Home-Verzeichnis des Benutzers gespeichert, das zur Laufzeit erstellt wird, falls es nicht existiert.
* Verwendet keine externen Abhängigkeiten für die Karte, sondern verwendet stattdessen eine bereits geschriebene HTML [Kartenvorlage](ipmap/data/templates/map.html).

# Installation
## PyPI
IPMap kann von PyPI aus installiert werden, indem Sie den folgenden Befehl im Terminal/in der Eingabeaufforderung ausführen
```
pip install ipmap
```
## GitHub
Wenn Sie es lieber von der Quelle installieren möchten, können Sie den folgenden Befehl ausführen
```
pip install git+https://github.com/rly0nheart/ipmap.git
```
## Aus dem Quellcode erstellen
```Python
# Poesie installieren
pip install poetry

# Klonen Sie das Projekt
git clone https://github.com/rly0nheart/ipmap

# in das ipmap-Verzeichnis verschieben
cd ipmap

# die Raddatei erstellen
poetry build

# das eingebaute Rad installieren (Linux)
pip install dist/*.whl

# Integriertes Rad installieren (Windows)
pip install .\dist\generated-wheel-file-name.whl
```

# Verwendung
Um die Nutzung zu sehen, können Sie einfach ausführen
```
ipmap --help
```
Die Ausgabe sollte wie folgt aussehen
```
Verwendung:
     IP-Adresse(n) geolokalisieren (mit einer interaktiven Karte)
     --------------------------------------------------
     ipmap map --ip <ip>

     Öffnen Sie Google Earth an den angegebenen Koordinaten
     ---------------------------------------------
     ipmap earth --ip <ip>

     IP-Adresse(n) suchen (wie Karte, aber ohne interaktive Karte)
     -------------------------------------------------- ----------------
     ipmap lookup --ip <ip>

Modi:
     map – erstellt eine interaktive Karte und zeigt die Standorte der angegebenen IP-Adresse(n) darauf an.
     earth – öffnet Google Earth am Standort der angegebenen IP-Adresse.
     lookup – sucht nach Informationen zu den angegebenen IP-Adressen.
    

IPMap (IP Mapper) – von Richard Mwewa (https://about.me/rly0nheart)

Positionsargumente:
   {earth,lookup,map}-Init-Modus

Optionen:
   -h, --help zeigt diese Hilfemeldung an und beendet den Vorgang
   -i IP, --ip IP IP
   -o AUSGABE, --output AUSGABE
                         Kartenausgabename (Standard-IPmap)
   -v, --version zeigt die Versionsnummer des Programms an und beendet das Programm

Ein plattformübergreifendes, benutzerfreundliches IP-Geolocation- und Mapping-Tool.
```
> Sie können auch eine Datei mit IP-Adressen an „--ip“ übergeben. IPMap verarbeitet die Datei entsprechend und liest jede IP Zeile für Zeile.
# Übersetzungen
* [Justin Clark](https://github.com/jclark1913) – [README_ar.md](https://github.com/rly0nheart/ipmap/blob/master/README_ar.md) für die arabische Übersetzung hinzugefügt
> Wenn Sie die README-Datei des Projekts in eine beliebige Sprache übersetzen möchten oder die (von Google übersetzten) Übersetzungen der bereits vorhandenen README-Dateien verbessern können, können Sie gerne eine Pull-Anfrage mit Ihren Übersetzungen öffnen. Ich würde sie gerne in das Projekt einbeziehen :).
