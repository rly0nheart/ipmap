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

IPMap 從文件中定位給定的 ip 地址/地址，然後生成一個 [leaflet](https://github.com/leaflet/leaflet) 地圖，精確定位每個 ip 地址的位置（使用正確的參數）。

＃ 特徵
- [x] 查找 ip 地址並返回相關信息。
- [x] 查找 ip 地址並返回相關信息，然後在生成的傳單地圖上指出 ip 地址的位置。
- [x] 在指定坐標（格式：緯度經度）上打開 Google 地球。
- [x] 生成的地圖將保存到運行時創建的 `maps` 目錄（如果不存在）。
- [x] 地圖不使用外部依賴項，而是使用已經編寫的 html ![地圖模板](ipmap/data/templates/map.html)。

＃ 安裝
## 派皮
可以通過在終端/命令提示符中運行以下命令從 PyPI 安裝 IPMap
```
pip install ipmap
```
## GitHub
或者，如果您更喜歡從源代碼安裝它，則可以運行以下命令
```
pip install git+https://github.com/rly0nheart/ipmap.git
```
## 從源代碼構建
```Python
# 安裝詩歌
pip install poetry

# 克隆項目
git clone https://github.com/rly0nheart/ipmap

# 移動到ipmap目錄
cd ipmap

# 構建 wheel 文件
poetry build

# 安裝內置的輪子 (Linux)
pip install dist/*.whl

# 安裝內置輪子 (Windows)
pip install .\dist\generated-wheel-file-name.whl
```

＃ 用法
要查看用法，您可以簡單地運行
```
ipmap --help
```
輸出應如下所示
```
用法：
     地理定位 IP 地址（帶有交互式地圖）
     ----------------------------------------------
     ipmap map --ip <ip/file_containing_ip_addresses>

     在給定的坐標上打開谷歌地球
     ------------------------------------------
     ipmap earth --coordinates <緯度> <經度>

     查找 IP 地址（與地圖相同，但沒有交互式地圖）
     ---------------------------------------------- ------------------
     ipmap lookup --ip <ip/file_containing_ip_addresses>

模式：
     map - 創建交互式地圖並在地圖上標明指定 IP 地址的位置。
     earth - 在指定的坐標上打開谷歌地球
     lookup - 查找指定的 IP 地址信息。
    

IPMap（IP 映射器）— 作者 Richard Mwewa (https://about.me/rly0nheart)

位置參數：
   {earth,lookup,map} 初始化模式

選項：
   -h, --help 顯示此幫助信息並退出
   -i IP, --ip IP 一個IP地址或一個包含IP地址的文件
   -o 輸出，--output
                         地圖輸出名稱
   -c 坐標坐標，--coordinates
                         空間分隔緯度和經度
   -v, --version 顯示程序的版本號並退出

一個跨平台的易於使用的 ip 地理定位和映射工具。
```
