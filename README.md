[![Docker Image CI](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml)
[![CodeQL](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml)
![GitHub top language](https://img.shields.io/github/languages/top/rly0nheart/ipmap?logo=github)
![PyPI](https://img.shields.io/pypi/v/ipmap?label=Latest%20Release&logo=pypi)
![PyPI - Status](https://img.shields.io/pypi/status/ipmap?label=Status&logo=pypi)

![English readme](README.md) • [简体中文 readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=zh-CN&_x_tr_hl=en&_x_tr_pto=wapp) • [正體中文 readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=zh-TW&_x_tr_hl=en&_x_tr_pto=wapp) • [Lengua española readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en&_x_tr_pto=wapp) • [Deutsche readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=de&_x_tr_hl=en&_x_tr_pto=wapp) • [Svenska readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=sv&_x_tr_hl=en&_x_tr_pto=wapp) • [한국어 readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=ko&_x_tr_hl=en&_x_tr_pto=wapp) • [Français readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en&_x_tr_pto=wapp) • [हिन्दी readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=hi&_x_tr_hl=en&_x_tr_pto=wapp) • [Português readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=en&_x_tr_pto=wapp) • [Italian readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=it&_x_tr_hl=en&_x_tr_pto=wapp)
 • [Русский readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=en&_x_tr_pto=wapp) • [Indonesian readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=en&_x_tr_pto=wapp) • [فارسی readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=fa&_x_tr_hl=en&_x_tr_pto=wapp) • [Türkçe readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=tr&_x_tr_hl=en&_x_tr_pto=wapp) • [Polskie readme](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=en&_x_tr_tl=pl&_x_tr_hl=en&_x_tr_pto=wapp)
 
 
IPMap geolocates a given ip address/addresses from a file, then generates a [leaflet](https://github.com/leaflet/leaflet) map pin-pointing the location of each ip address on it (with the right argument).

# Features
- [x] Looks up ip address(es) and returns the associated information.
- [x] Looks up an ip address(es) and returns the associated information then pin points the location of the ip address(es) on a generated leaflet map.
- [x] Opens Google Earth on the specified coordinates (format: latitude longitude).
- [x] Generated maps are saved to the `maps` directory which is created on runtime if it does not exist.
- [x] Does not use external dependencies for the map, instead uses an already written html ![map template](ipmap/data/templates/map.html).

# Installation
## PyPI
IPMap can be installed from PyPI by running the folloing command in terminal/command prompt
```
pip install ipmap
```
## GitHub
Or if you prefer to install it from source, you can run the following command
```
pip install git+https://github.com/rly0nheart/ipmap.git
```
## Build from source
```Python
# install poetry
pip install poetry

# clone the project
git clone https://github.com/rly0nheart/ipmap

# move to the ipmap directory
cd ipmap

# build the wheel file
poetry build

# install the built wheel (Linux)
pip install dist/*.whl

# install built wheel (Windows)
pip install .\dist\generated-wheel-file-name.whl
```

# Usage
To see the usage, you can simply run
```
ipmap --help
```
The output should look like the following
```
usage: 
    Geolocate IP Address(es) (with an interactive map)
    --------------------------------------------------
    ipmap map --ip <ip/file_containing_ip_addresses>

    Open Google Earth on the given coordinates
    --------------------------------------------
    ipmap earth --coordinates <latitude> <longitude>

    Lookup IP Address(es) (same as map but without an interactive map)
    ------------------------------------------------------------------
    ipmap lookup --ip <ip/file_containing_ip_addresses>

modes:
    map - creates an interactive map and pin points the locations of the specified ip address(es) on it.
    earth - opens google earth on the specified coordinates
    lookup - looks up the specified ip address(es)' information.
    

IPMap (IP Mapper) — by Richard Mwewa (https://about.me/rly0nheart)

positional arguments:
  {earth,lookup,map}    init mode

options:
  -h, --help            show this help message and exit
  -i IP, --ip IP        an ip address or a file containing ip addresses
  -o OUTPUT, --output OUTPUT
                        map output name
  -c COORDINATES COORDINATES, --coordinates COORDINATES COORDINATES
                        space separated latitude and longitude
  -v, --version         show program's version number and exit

A cross-platform easy-to-use ip geolocation & mapping tool.
```
