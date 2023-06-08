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

<div dir="rtl">
يحدد تطبيق (IPMap) الموقع الجغرافي لعنوان IP أو عدد من عناوين IP من ملف ثم ينشئ خريطة من نوع [leaflet] (https://github.com/leaflet/leaflet) تشير إلى الموقع الجغرافي لكل عنوان IP موجود في ذات الملف.

# الميّزات
* البحث عن عنوان/عناوين IP وإرجاع المعلومات المتعلقة بها.
* تحديد المواقع الجغرافية لعنوان/عناوين IP والإشارة إليها في خريطة من نوع leaflet يتم إنشاؤها بواسطة التطبيق.
* عرض إحداثيات المواقع الجغرافية لعنوان/عناوين IP في برنامج Google Earth.
* حفظ الخرائط التي تم إنشاؤها في دليل ملفات اسمه `maps` والذي يتم إنشاؤه عند تشغيل التطبيق إن لم يكن موجود مسبقاً.
* عدم وجود أيّ تبعيات خارجية: يستخدم التطبيق ملف html تم إعداده مسبقاً لإنشاء الخرائط. ![map template](ipmap/data/templates/map.html).


# تعليمات التثبيت

## PyPI
يمكن تثبيت IPMap من خلال PyPI عن طريق استخدام الأمر التالي في المحطة الطرفية/سطر الأوامر:
```
pip install  ipmap
```
## GitHub
يمكن تثبيت IPMap عن طريق المستودع المصدري على  Github باستخدام الأمر التالي:
```
pip install git+https://github.com/rly0nheart/ipmap.git
```

## التثبيت من المستودع المصدري
```python
# ثبّت poetry
pip install poetry

# استنسخ المستودع
git clone https://github.com/rly0nheart/ipmap

# التوجه الى دليل الملفات ipmap
cd ipmap

# اعمل ملف "wheel"
poetry build

# ثبّت ملف الـ"wheel" (لينوكس)
pip install dist/*.whl

# ثبّت ملف الـ"wheel" (ويندوز)
pip install .\dist\generated-wheel-file-name.whl

```

# الاستخدام
لكشف دليل الاستخدام، استخدم الامر التالي:

```
ipmap --help
```
من المفترض أن تظهر التنيجة التالية:

```
usage:
    Geolocate IP Address(es) (with an interactive map)
    --------------------------------------------------
    ipmap map --ip <ip>

    Open Google Earth on the given coordinates
    --------------------------------------------
    ipmap earth --ip <ip>

    Lookup IP Address(es) (same as map but without an interactive map)
    ------------------------------------------------------------------
    ipmap lookup --ip <ip>

modes:
    map - creates an interactive map and pin points the locations of the specified ip address(es) on it.
    earth - opens google earth on the location of the given ip address.
    lookup - looks up the specified ip address(es)' information.


IPMap (IP Mapper) — by Richard Mwewa (https://about.me/rly0nheart)

positional arguments:
  {earth,lookup,map}    init mode

options:
  -h, --help            show this help message and exit
  -i IP, --ip IP        ip
  -o OUTPUT, --output OUTPUT
                        map output name (default ipmap)
  -v, --version         show program's version number and exit

A cross-platform easy-to-use ip geolocation & mapping tool.
```
> يمكنك أيضا إيضاع ملف يحتوي على عناوين IP في المحطة الطرفية باستخدام `--ip`. في هذه حالة، سيقرأ IPMap كل عنوان في ذات الملف سطراً بسطر.
# الترجمة
* [Justin Clark](https://github.com/jclark1913) - اضافة ترجمة باللغة العربية [README_ar.md](https://github.com/rly0nheart/ipmap/blob/master/README_ar.md)
> في حال رغبت في ترجمة ملف الـREADME لهاد المشروع إلى اي لغة أو أردت تحسين الملفات التي تم ترجمتها عبر Google Translate فبإمكانك فتح طلب سحب مع ترجمتك وسأكون سعيداً جداً لإضافتها إلى المشروع :)
</div>
