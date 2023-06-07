[![Docker Image CI](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml)
[![CodeQL](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml)
![GitHub top language](https://img.shields.io/github/languages/top/rly0nheart/ipmap?logo=github)
![PyPI](https://img.shields.io/pypi/v/ipmap?label=Latest%20Release&logo=pypi)
![PyPI - Status](https://img.shields.io/pypi/status/ipmap?label=Status&logo=pypi)

![English readme](README.md) • ![简体中文 readme](README_zh-CH.md) • ![正體中文 readme](README_zh-TW) • ![Lengua española readme](README_es.md) • ![Deutsche readme](README_de,md) • ![Svenska readme](README_sv.md) • ![한국어 readme](README_kr.md) • [Français readme](README_fr.md) • ![हिन्दी readme](README_hi.md) • ![Português readme](README_pt.md) • ![Italian readme](README_it.md)
 • ![Русский readme](README_ru.md) • [Indonesian readme](README_id.md) • ![فارسی readme](README_fa.md) • ![Türkçe readme](README_tr.md) • ![Polskie readme](README_pl.md)

IPMap geolocaliza una dirección IP dada/direcciones de un archivo, luego genera un [folleto] (https://github.com/leaflet/leaflet) mapa que señala la ubicación de cada dirección IP en él (con el argumento correcto).

# Características
- [x] Busca direcciones IP y devuelve la información asociada.
- [x] Busca una(s) dirección(es) IP y devuelve la información asociada, luego señala la ubicación de la(s) dirección(es) IP en un mapa de folleto generado.
- [x] Abre Google Earth en las coordenadas especificadas (formato: latitud longitud).
- [x] Los mapas generados se guardan en el directorio `maps` que se crea en tiempo de ejecución si no existe.
- [x] No utiliza dependencias externas para el mapa, sino que utiliza un html ya escrito. [Plantilla de mapa] (ipmap/data/templates/map.html).

# Instalación
## PyPI
IPMap se puede instalar desde PyPI ejecutando el siguiente comando en la terminal/símbolo del sistema
```
pip install ipmap
```
## GitHub
O si prefiere instalarlo desde la fuente, puede ejecutar el siguiente comando
```
pip install git+https://github.com/rly0nheart/ipmap.git
```
## Construir desde la fuente
```Python
# instalar poesía
pip install poetry

# clonar el proyecto
git clone https://github.com/rly0nheart/ipmap

# mover al directorio ipmap
cd ipmap

# construir el archivo de la rueda
poetry build

# instalar la rueda integrada (Linux)
pip install dist/*.whl

# instalar rueda integrada (Windows)
pip install .\dist\generated-wheel-file-name.whl
```

# Uso
Para ver el uso, simplemente puede ejecutar
```
ipmap --help
```
La salida debe verse como la siguiente
```
uso:
     Geolocalizar direcciones IP (con un mapa interactivo)
     --------------------------------------------------
     ipmap map --ip <ip/file_containing_ip_addresses>

     Abre Google Earth en las coordenadas dadas
     --------------------------------------------
     ipmap earth --coordenadas <latitud> <longitud>

     Búsqueda de direcciones IP (igual que el mapa pero sin un mapa interactivo)
     -------------------------------------------------- ----------------
     ipmap lookup --ip <ip/file_containing_ip_addresses>

modos:
     mapa: crea un mapa interactivo y señala las ubicaciones de las direcciones IP especificadas en él.
     tierra - abre Google Earth en las coordenadas especificadas
     búsqueda: busca la información de la(s) dirección(es) IP especificada(s).
    

IPMap (Asignador de IP) — por Richard Mwewa (https://about.me/rly0nheart)

argumentos posicionales:
   modo de inicio {earth, lookup, map}

opciones:
   -h, --help muestra este mensaje de ayuda y sale
   -i IP, --ip IP una dirección IP o un archivo que contiene direcciones IP
   -o SALIDA, --output SALIDA
                         nombre de salida del mapa
   -c COORDENADAS COORDENADAS, --coordinates COORDENADAS COORDENADAS
                         espacio separado latitud y longitud
   -v, --version muestra el número de versión del programa y sale

Una herramienta de mapeo y geolocalización IP multiplataforma fácil de usar.
```
