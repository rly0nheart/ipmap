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

IPMap geolocaliza una dirección IP dada/direcciones de un archivo, luego genera un [folleto mapa](https://github.com/leaflet/leaflet) que señala la ubicación de cada dirección IP en él (con el argumento correcto).

# Características
* Busca direcciones IP y devuelve la información asociada.
* Busca una (s) dirección (es) IP y devuelve la información asociada, luego señala la ubicación de la (s) dirección (es) IP en un mapa de folleto generado.
* Abre Google Earth en la ubicación de las direcciones IP especificadas.
* Los mapas generados se guardan en el directorio `maps` en el directorio de inicio del usuario que se crea en tiempo de ejecución si no existe.
* No utiliza dependencias externas para el mapa, sino que utiliza una [plantilla de mapa] html ya escrita (ipmap/data/templates/map.html).

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
```Pitón
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
     ipmap map --ip <ip>

     Abre Google Earth en las coordenadas dadas
     --------------------------------------------
     ipmap earth --ip <ip>

     Búsqueda de direcciones IP (igual que el mapa pero sin un mapa interactivo)
     -------------------------------------------------- ----------------
     ipmap lookup --ip <ip>

modos:
     map - crea un mapa interactivo y señala las ubicaciones de las direcciones IP especificadas en él.
     earth - abre Google Earth en la ubicación de la dirección IP dada.
     lookup - busca la información de la(s) dirección(es) IP especificada(s).
    

IPMap (Asignador de IP) — por Richard Mwewa (https://about.me/rly0nheart)

argumentos posicionales:
   modo de inicio {earth, lookup, map}

opciones:
   -h, --help muestra este mensaje de ayuda y sale
   -i IP, --ip IP ip
   -o SALIDA, --output SALIDA
                         nombre de salida del mapa (ipmap predeterminado)
   -v, --version muestra el número de versión del programa y sale

Una herramienta de mapeo y geolocalización IP multiplataforma fácil de usar.
```
> También puede pasar un archivo que contenga direcciones IP a `--ip`, IPMap procesará el archivo en consecuencia y leerá cada IP línea por línea.
# Traducciones
* [Justin Clark](https://github.com/jclark1913) - Se agregó [README_ar.md](https://github.com/rly0nheart/ipmap/blob/master/README_ar,md) para la traducción al árabe
> Si desea traducir el LÉAME del proyecto a cualquier idioma, o si puede mejorar las traducciones (traducidas por Google) de los LÉAME ya existentes, no dude en abrir una solicitud de extracción con sus traducciones. Estaría más que feliz de incluirlos en el proyecto :).
