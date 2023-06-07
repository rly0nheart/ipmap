[![Docker Image CI](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml)
[![CodeQL](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml)
![GitHub top language](https://img.shields.io/github/languages/top/rly0nheart/ipmap?logo=github)
![PyPI](https://img.shields.io/pypi/v/ipmap?label=Latest%20Release&logo=pypi)
![PyPI - Status](https://img.shields.io/pypi/status/ipmap?label=Status&logo=pypi)

![English readme](README.md) • ![简体中文 readme](README_zh-CN.md) • ![正體中文 readme](README_zh-TW.md) • ![Lengua española readme](README_es.md) • ![Deutsche readme](README_de,md) • ![Svenska readme](README_sv.md) • ![한국어 readme](README_kr.md) • [Français readme](README_fr.md) • ![हिन्दी readme](README_hi.md) • ![Português readme](README_pt.md) • ![Italian readme](README_it.md)
 • ![Русский readme](README_ru.md) • [Indonesian readme](README_id.md) • ![فارسی readme](README_fa.md) • ![Türkçe readme](README_tr.md) • ![Polskie readme](README_pl.md)

IPMap lokalisiert eine oder mehrere bestimmte IP-Adressen aus einer Datei und generiert dann eine [Leaflet](https://github.com/leaflet/leaflet)-Karte, die den Standort jeder darauf befindlichen IP-Adresse genau angibt (mit dem richtigen Argument).

# Merkmale
- [x] Sucht nach IP-Adresse(n) und gibt die zugehörigen Informationen zurück.
- [x] Sucht nach einer oder mehreren IP-Adressen und gibt die zugehörigen Informationen zurück. Anschließend wird der Standort der IP-Adresse(n) auf einer generierten Prospektkarte lokalisiert.
- [x] Öffnet Google Earth an den angegebenen Koordinaten (Format: Breitengrad und Längengrad).
- [x] Generierte Karten werden im Verzeichnis „maps“ gespeichert, das zur Laufzeit erstellt wird, falls es nicht existiert.
- [x] Verwendet keine externen Abhängigkeiten für die Karte, sondern verwendet stattdessen eine bereits geschriebene HTML-Datei ![Kartenvorlage](ipmap/data/templates/map.html).

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
     ipmap map --ip <ip/file_tained_ip_addresses>

     Öffnen Sie Google Earth an den angegebenen Koordinaten
     ---------------------------------------------
     ipmap earth --coordinates <Breitengrad> <Längengrad>

     IP-Adresse(n) suchen (wie Karte, aber ohne interaktive Karte)
     -------------------------------------------------- ----------------
     ipmap lookup --ip <IP/Datei_mit_IP-Adressen>

Modi:
     map – erstellt eine interaktive Karte und zeigt die Standorte der angegebenen IP-Adresse(n) darauf an.
     earth – öffnet Google Earth an den angegebenen Koordinaten
     lookup – sucht nach Informationen zu den angegebenen IP-Adressen.
    

IPMap (IP Mapper) – von Richard Mwewa (https://about.me/rly0nheart)

Positionsargumente:
   {earth,lookup,map}-Init-Modus

Optionen:
   -h, --help zeigt diese Hilfemeldung an und beendet den Vorgang
   -i IP, --ip IP eine IP-Adresse oder eine Datei mit IP-Adressen
   -o AUSGABE, --output AUSGABE
                         Name der Kartenausgabe
   -c KOORDINATEN KOORDINATEN, --coordinates KOORDINATEN KOORDINATEN
                         durch Leerzeichen getrennter Breiten- und Längengrad
   -v, --version zeigt die Versionsnummer des Programms an und beendet das Programm

Ein plattformübergreifendes, benutzerfreundliches IP-Geolocation- und Mapping-Tool.
```
