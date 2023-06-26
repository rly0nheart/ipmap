[![Docker Image CI](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml)
[![CodeQL](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml)
![GitHub top language](https://img.shields.io/github/languages/top/rly0nheart/ipmap?logo=github)
![PyPI](https://img.shields.io/pypi/v/ipmap?label=Latest%20Release&logo=pypi)
![PyPI - Status](https://img.shields.io/pypi/status/ipmap?label=Status&logo=pypi)

[English](https://github.com/rly0nheart/ipmap/blob/master/README.md) •
[简体中文](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=zh-CN&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[正體中文](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=zh-TW&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Lengua española](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Deutsche](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=de&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Svenska](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=sv&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[한국어](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=ko&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Français](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=fr&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[हिन्दी](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=hi&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Português](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=pt&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Italian](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=it&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Русский](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=ru&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Indonesian](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=id&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[فارسی](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=fa&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[عربي](https://github.com/rly0nheart/ipmap/blob/master/README_ar.md) •
[Türkçe](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=tr&_x_tr_hl=en-US&_x_tr_pto=wapp) •
[Polskie](https://github-com.translate.goog/rly0nheart/ipmap/blob/master/README.md?_x_tr_sl=auto&_x_tr_tl=pl&_x_tr_hl=en-US&_x_tr_pto=wapp)

IPMap geolocates a given ip address/addresses from a file, then generates a [leaflet](https://github.com/leaflet/leaflet) map pin-pointing the location of each ip address on it (with the right argument).

# Features
* Looks up ip address(es) and returns the associated information.
* Looks up an ip address(es) and returns the associated information then pin points the location of the ip address(es) on a generated leaflet map.
* Opens Google Earth on the location of the specified ip address(es).
* Generated maps are saved to the `maps` directory in the user's home directory which is created on runtime if it does not exist.
* Does not use external dependencies for the map, instead uses an already written html [map template](ipmap/data/templates/map.html).

# Installation
## PyPI
IPMap can be installed from PyPI by running the following command in terminal/command prompt
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
> You can also pass a file containing ip addresses to `--ip`, IPMap will process the file accordingly and read each ip line by line.
# Translations
* [Justin Clark](https://github.com/jclark1913) - Added [README_ar.md](https://github.com/rly0nheart/ipmap/blob/master/README_ar.md) for Arabic translation
> If you'd like to translate the project's README in any language, or if you can improve the (Google translated) translations of the already existing README's, feel free to open a pull request with your translations. I'd be more than happy to include them in the project :).
