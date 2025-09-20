# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from datetime import datetime
from w3lib.html import remove_tags

def clean_text(value):
    return value.replace('\n','').strip()
    
def clean_price(value):
    try:
        return float(value.replace('Gs.','').replace('.','').strip())
    except ValueError:
        return None


class StoreItem(scrapy.Item):
    # define the fields for your item here like:
   
   #input processors are declared using the _in suffix while output 
   #processors are declared using the _out suffix.
    Nro=scrapy.Field(output_processor=TakeFirst())
    Description=scrapy.Field(input_processor=MapCompose(remove_tags, clean_text),output_processor=TakeFirst())
    Price=scrapy.Field(input_processor=MapCompose(remove_tags, clean_price),output_processor=TakeFirst())
    
class UrlItem(scrapy.Item):
    Nro=scrapy.Field(output_processor=TakeFirst())
    Image=scrapy.Field(output_processor=TakeFirst())
    Link=scrapy.Field(output_processor=TakeFirst())
    Socials=scrapy.Field(output_processor=TakeFirst())

class CacheItem(scrapy.Item):
    #TODO
    #cache info
            #l.add_value('url',response.url)
            #l.add_value('headers',response.headers)
            #l.add_value('ip',response.ip_address)
    url=scrapy.Field(output_processor=TakeFirst())
    header=scrapy.Field(output_processor=TakeFirst())
    #ipv4=scrapy.Field(output_processor=TakeFirst())
