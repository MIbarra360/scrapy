import scrapy
from scrapy.http import Response
from ..items import StoreItem
from datetime import date
from scrapy.loader import ItemLoader


class webscrapSpider(scrapy.Spider):
    name = "webscrap"
    allowed_domains = ["nissei.com"]
    start_urls = ["https://nissei.com/py/electronica?am_on_sale=1&cat=131&p=2"]

    today = date.today().strftime("%d_%m_%Y")
    custom_settings = {
        'FEEDS': {
            f"{today}.json": {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': ['Nro','Description', 'Price', 'Image','Link','Socials'],
                'overwrite': True,
            },
        }
    }

    def parse(self, response: Response):

        self.logger.info("Parse function called on %s", response.url)

        for nro, product in enumerate (response.css('.item.product.product-item'),start=1):
            #The "selector" to extract data from, when using the add_xpath() n' add_css() method.
            l=ItemLoader(item=StoreItem(),selector=product)
            l.add_value('Nro',nro)
            l.add_css('Description','.product-item-link::text')
            l.add_css('Price','.price::text')
            l.add_css('Image','.product-image-photo::attr(data-src)')
            l.add_xpath('Link','.//div/h2/a/@href')
            #REVIEW
            #FIXME
            # load stuff not in the footer
            footer=l.nested_css('.ul.social-links')
            footer.add_css('Socials','#footer-widgets > div > div:first-child > div > div:first-child > ul > ul > li:first-child > a::attr(href)')
            # no need to call footer.load_item()
            yield l.load_item()
