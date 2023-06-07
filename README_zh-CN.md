[![Docker Image CI](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/docker-image.yml)
[![CodeQL](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml/badge.svg)](https://github.com/rly0nheart/ipmap/actions/workflows/codeql.yml)
![GitHub top language](https://img.shields.io/github/languages/top/rly0nheart/ipmap?logo=github)
![PyPI](https://img.shields.io/pypi/v/ipmap?label=Latest%20Release&logo=pypi)
![PyPI - Status](https://img.shields.io/pypi/status/ipmap?label=Status&logo=pypi)

![English readme](README.md) • ![简体中文 readme](README_zh-CN.md) • ![正體中文 readme](README_zh-TW.md) • ![Lengua española readme](README_es.md) • ![Deutsche readme](README_de,md) • ![Svenska readme](README_sv.md) • ![한국어 readme](README_kr.md) • [Français readme](README_fr.md) • ![हिन्दी readme](README_hi.md) • ![Português readme](README_pt.md) • ![Italian readme](README_it.md)
 • ![Русский readme](README_ru.md) • [Indonesian readme](README_id.md) • ![فارسی readme](README_fa.md) • ![Türkçe readme](README_tr.md) • ![Polskie readme](README_pl.md)

IPMap 从文件中定位给定的 ip 地址/地址，然后生成一个 [leaflet](https://github.com/leaflet/leaflet) 地图，精确定位每个 ip 地址的位置（使用正确的参数）。

＃ 特征
- [x] 查找 ip 地址并返回相关信息。
- [x] 查找 ip 地址并返回相关信息，然后在生成的传单地图上指出 ip 地址的位置。
- [x] 在指定坐标（格式：纬度经度）上打开 Google 地球。
- [x] 生成的地图将保存到运行时创建的 `maps` 目录（如果不存在）。
- [x] 地图不使用外部依赖项，而是使用已经编写的 html ![地图模板](ipmap/data/templates/map.html)。

＃ 安装
## 派皮
可以通过在终端/命令提示符中运行以下命令从 PyPI 安装 IPMap
```
pip install ipmap
```
## GitHub
或者，如果您更喜欢从源代码安装它，则可以运行以下命令
```
pip install git+https://github.com/rly0nheart/ipmap.git
```
## 从源代码构建
```Python
# 安装诗歌
pip install poetry

# 克隆项目
git clone https://github.com/rly0nheart/ipmap

# 移动到ipmap目录
cd ipmap

# 构建 wheel 文件
poetry build

# 安装内置的轮子 (Linux)
pip install dist/*.whl

# 安装内置轮子 (Windows)
pip install .\dist\generated-wheel-file-name.whl
```

＃ 用法
要查看用法，您可以简单地运行
```
ipmap --help
```
输出应如下所示
```
用法：
     地理定位 IP 地址（带有交互式地图）
     ----------------------------------------------
     ipmap map --ip <ip/file_containing_ip_addresses>

     在给定的坐标上打开谷歌地球
     ------------------------------------------
     ipmap earth --coordinates <纬度> <经度>

     查找 IP 地址（与地图相同，但没有交互式地图）
     ---------------------------------------------- ------------------
     ipmap lookup --ip <ip/file_containing_ip_addresses>

模式：
     map - 创建交互式地图并在地图上标明指定 IP 地址的位置。
     earth - 在指定的坐标上打开谷歌地球
     lookup - 查找指定的 IP 地址信息。
    

IPMap（IP 映射器）— 作者 Richard Mwewa (https://about.me/rly0nheart)

位置参数：
   {earth,lookup,map} 初始化模式

选项：
   -h, --help 显示此帮助信息并退出
   -i IP, --ip IP 一个IP地址或一个包含IP地址的文件
   -o 输出，--output
                         地图输出名称
   -c 坐标坐标，--coordinates
                         空间分隔纬度和经度
   -v, --version 显示程序的版本号并退出

一个跨平台的易于使用的 ip 地理定位和映射工具。
```
