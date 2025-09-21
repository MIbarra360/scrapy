import scrapy
from scrapy.http import Response, Request
from ..items import StoreItem, UrlItem
from datetime import date
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from colorama import Fore, Style
def uri_params(params, spider): #could bein settings
        today = date.today().strftime("%d_%m_%Y")
        return {**params, "spider": spider.name, "time":today}

class webscrapSpider(scrapy.Spider):
    name = "webscrap"
    allowed_domains = ["nissei.com"]
    start_urls = ["https://nissei.com/py/electronica?am_on_sale=1&cat=131&p=2"]

#-------------------------------------------------------# 

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            #---------------------
            self.produc_counter=0   #enumerate products

        # https://docs.scrapy.org/en/latest/topics/link-extractors.html   
        #The __init__ method of LxmlLinkExtractor takes settings
        #that determine which links may be extracted
            self.link_extractor = LinkExtractor(allow=r"cat=131&p=\d+")
#-------------------------------------------------------#
    
    custom_settings = {
        "FEEDS": {
            "data/%(spider)s-%(time)s.json": {
                "format": "json",
                "encoding": "utf8",
                "store_empty": False,
                "fields": ["Nro", "Description", "Price"],
                "overwrite": True,
                "item_classes":["store.items.StoreItem"]
            },
            "data/urls-%(spider)s-%(time)s.json": {
                "format": "json",
                "store_empty": False,
                "fields": ["Nro", "Image", "Link", "Socials"],
                "overwrite": True,
                "item_classes":["store.items.UrlItem"]
            },
            
        },
        "FEED_URI_PARAMS": uri_params,
    }

    def parse(self, response: Response):

        self.logger.info(Fore.RED + f">>> Parse function called on {Fore.BLUE}{response.url}" + Style.RESET_ALL)

        for product in response.css('.item.product.product-item'):

            self.produc_counter+=1 

            #The "selector" to extract data from, when using the add_xpath() n' add_css() method.
            l=ItemLoader(item=StoreItem(),selector=product)
            l.add_value('Nro',self.produc_counter)
            l.add_css('Description','.product-item-link::text')
            l.add_css('Price','.price::text')
            yield l.load_item()
    #------SAVE IMAGES links AND PRODUCT links--------
            l2=ItemLoader(item=UrlItem(),selector=product)
            l2.add_value('Nro',self.produc_counter)
            l2.add_css('Image','.product-image-photo::attr(data-src)')
            l2.add_xpath('Link','.//div/h2/a/@href')
            #REVIEW
            #FIXME
            # load stuff not in the footer
            footer=l2.nested_css('ul.social-links')
            footer.add_css('Socials', 'ul.social-links li a::attr(href)')
            yield l2.load_item()
    #------ --------
        #REVIEW: 
        for link in self.link_extractor.extract_links(response):

            yield Request(link.url, callback=self.parse)
