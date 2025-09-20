# scrapy
This is a example web scraping

## Requirements
* Scrapy 2.13.3+ 
* Python 3.13.1+

## Instruction

```bash
git clone https://github.com/MIbarra360/scrapy.git
pip install -r requirements.txt
scrapy crawl webscrap
```

## Output

The `data`📁 folder contains the Output

### example:

**📁data/webscrap-20_09_2025.json**

 ```json
[
{"Nro": 1, "Description": "Xiaomi Poco C75 Dual", "Price": 959000.0},
{"Nro": 2, "Description": "Honor X5b Plus Dual 256 GB - Ocean Blue", "Price": 990000.0},
{"Nro": 3, "Description": "Honor X5b Plus Dual 256 GB - Midnight Black", "Price": 990000.0},
{"Nro": 4, "Description": "Honor X5b Plus Dual 256 GB", "Price": 990000.0},
{"Nro": 5, "Description": "HMD Aura TA-1637 Dual 128 GB - Verde", "Price": 679000.0},
{"Nro": 6, "Description": "HMD Aura TA-1637 Dual 128 GB - Negro", "Price": 679000.0},
```

**📁data/cache-20_09_2025.json**

 ```json
[
{"url": "https://nissei.com/py/electronica?am_on_sale=1&cat=131&p=2", "header": {"Content-Length": "67589", "Date": "Sat, 20 Sep 2025 18:54:04 GMT", "Content-Type": "text/html; charset=UTF-8", "X-Content-Type-Options": "nosniff", "X-Xss-Protection": "1; mode=block", "X-Frame-Options": "app.powerbi.com", "Vary": "Accept-Encoding", "Accept-Ranges": "bytes", "Pragma": "no-cache", "Expires": "-1", "Cache-Control": "public, max-age=2592000", "Alt-Svc": "h3-27=\":8889\"; ma=86400, h3-28=\":8889\"; ma=86400, h3-29=\":8889\"; ma=86400", "Content-Security-Policy": "default-src * 'unsafe-inline' 'unsafe-eval'; script-src * 'unsafe-inline' 'unsafe-eval'; worker-src 'self' blob:; connect-src * 'unsafe-inline'; img-src * data: blob: 'unsafe-inline'; frame-src *; style-src * 'unsafe-inline'; form-action * 'unsafe-inline'; font-src * data:;"}}
]
```

**📁data/urls-20_09_2025.json**

```json
[
{"Nro": 1, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/0/N/0N3qdpGCXuiHLKCWngFUq0wRUhLKDUPe41y.jpg", "Link": "https://nissei.com/py/electronica/xiaomi-poco-c75-dual"},
{"Nro": 2, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/m/4/m4FNfA8ikigOiMQljxb3960vSKelbHo8as6.jpg", "Link": "https://nissei.com/py/electronica/honor-x5b-plus-dual-256-gb-ocean-blue"},
{"Nro": 3, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/R/k/RkxJ0S2yezqFpGPbx1WONoT8QBJodKJcN7Y.jpg", "Link": "https://nissei.com/py/electronica/cel-honor-x5b-plus-dual-256gb-4gb-midnight-black"},
{"Nro": 4, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/W/5/W5pFOyXeMiUVh6gbU4Cdn5TMbP2XHXieeTj.jpg", "Link": "https://nissei.com/py/electronica/honor-x5b-plus-dual-256-gb"},
```
