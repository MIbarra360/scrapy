# scrapy
This is a example web scraping

## Requirements
* Python 3.13.1+
* Scrapy 2.13.3+ 
* colorama 0.4.6

## Instruction

```bash
git clone https://github.com/MIbarra360/scrapy.git
cd scrapy
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```
### To run the spider:
```bash
scrapy crawl webscrap
```

# Output

The `data`📁 folder contains the Output

### example:

**📁`data`/`webscrap-01_01_2025.json`**

 ```json
[
{"Nro": 1, "Description": "Honor X5b Plus Dual 256 GB - Ocean Blue", "Price": 990000.0},
{"Nro": 2, "Description": "Honor X5b Plus Dual 256 GB - Midnight Black", "Price": 990000.0},
{"Nro": 3, "Description": "Honor X5b Plus Dual 256 GB", "Price": 990000.0},
{"Nro": 4, "Description": "HMD Aura TA-1637 Dual 128 GB - Verde", "Price": 679000.0},
{"Nro": 5, "Description": "HMD Aura TA-1637 Dual 128 GB - Negro", "Price": 679000.0},
{"Nro": 6, "Description": "HMD Aura TA-1637 Dual", "Price": 679000.0},
{"Nro": 7, "Description": "HMD Pulse Pro TA-1606 Dual 256 GB - Negro", "Price": 1190000.0},
{"Nro": 8, "Description": "HMD Pulse Pro TA-1606 Dual 256 GB - Verde", "Price": 1190000.0},
{"Nro": 9, "Description": "HMD Pulse Pro TA-1606 Dual", "Price": 1190000.0},
{"Nro": 10, "Description": "HMD Barbie TA-1681 Dual - Rosa", "Price": 469000.0},
```

**📁`data`/`stats-webscrap-01_01_2025.json`**

 ```json
{
    "log_count/DEBUG": 154,
    "log_count/INFO": 12,
    "start_time": "2025-01-01 18:59:00.906424+00:00",
    "scheduler/enqueued/memory": 2,
    "scheduler/enqueued": 2,
    "scheduler/dequeued/memory": 2,
    "scheduler/dequeued": 2,
    "downloader/request_count": 2,
    "downloader/request_method_count/GET": 2,
    "downloader/request_bytes": 773,
    "downloader/response_count": 2,
    "downloader/response_status_count/200": 2,
    "downloader/response_bytes": 136160,
    "httpcompression/response_bytes": 1520098,
    "httpcompression/response_count": 2,
    "response_received_count": 2,
```

**📁`data`/`urls-webscrap-01_01_2025.json`**

```json
[
{"Nro": 1, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/m/4/m4FNfA8ikigOiMQljxb3960vSKelbHo8as6.jpg", "Link": "https://nissei.com/py/electronica/honor-x5b-plus-dual-256-gb-ocean-blue"},
{"Nro": 2, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/R/k/RkxJ0S2yezqFpGPbx1WONoT8QBJodKJcN7Y.jpg", "Link": "https://nissei.com/py/electronica/cel-honor-x5b-plus-dual-256gb-4gb-midnight-black"},
{"Nro": 3, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/W/5/W5pFOyXeMiUVh6gbU4Cdn5TMbP2XHXieeTj.jpg", "Link": "https://nissei.com/py/electronica/honor-x5b-plus-dual-256-gb"},
{"Nro": 4, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/r/0/r0SwOw7XMnmORGTlw7scXuNDuLfi6kj3cnZ.jpg", "Link": "https://nissei.com/py/electronica/hmd-aura-ta-1637-dual-128-gb-verde"},
{"Nro": 5, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/8/2/82QGyfAEe8QRlpJvmHUCRnqRRUFWqqzjR1V.jpg", "Link": "https://nissei.com/py/electronica/hmd-aura-ta-1637-dual-128-gb-negro"},
{"Nro": 6, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/r/0/r0swow7xmnmorgtlw7scxundulfi6kj3cnz.jpg", "Link": "https://nissei.com/py/electronica/hmd-aura-ta-1637-dual"},
{"Nro": 7, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/T/Q/TQT6jnWNkjzWNQaHCZYkqAiqJh8m5vxOzNw.jpg", "Link": "https://nissei.com/py/electronica/hmd-pulse-pro-ta-1606-dual-256-gb-negro"},
{"Nro": 8, "Image": "https://nissei.com/media/catalog/product/cache/515ce00244062f68c34ce5aef51078ec/6/r/6rNpWghYSVlNVx7ZjRwiWCW5msqoZKGuJGf.jpg", "Link": "https://nissei.com/py/electronica/hmd-pulse-pro-ta-1606-dual-256-gb-verde"},
```
