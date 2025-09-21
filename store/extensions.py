from colorama import Fore, Style
from scrapy import signals
import json
from datetime import date

#from scrapy.statscollectors

'''https://docs.scrapy.org/en/latest/topics/stats.html
   https://docs.scrapy.org/en/1.3/topics/exporters.html
Scrapy provides a convenient facility for collecting stats in the form of key/values,
 where values are often counters. The facility is called the Stats Collector,
   and can be accessed through the stats attribute of the Crawler API,'''

class ExtensionThatAccessStats:
    def __init__(self, stats):
        self.stats = stats
        self.today = date.today().strftime("%d_%m_%Y")
    @classmethod
    def from_crawler(cls, crawler):
        ext=cls(crawler.stats)
    #class SignalManager:
        #def connect(self, receiver: Any, signal: Any, **kwargs: Any) -> None:
        crawler.signals.connect(ext.spider_closed, signals.spider_closed)
        crawler.signals.connect(ext.spider_opened, signals.spider_opened)
        return ext
    
    def spider_opened(self, spider):
        spider.logger.info(f"{Fore.RED}>>> THE SPIDER:{Fore.BLUE} {spider.name}{Fore.RED} is opened{Style.RESET_ALL}")

    def spider_closed(self, spider):
        #Get stat value:
        #>>> stats.get_value("custom_count")
        #1
        stats=self.stats.get_stats()#Get all stats:
        #spider.logger.info(Fore.RED +str(stats)+ Style.RESET_ALL)
                            #red_color + str() + reset_color
        spider.logger.info(f"\n{Fore.RED}>>> See the output in{Fore.GREEN} data {Fore.RED}folder:"
                           f"\n{Fore.RED} > {Fore.GREEN}data/{Fore.BLUE}{spider.name}-{self.today}.json"
                           f"\n{Fore.RED} > {Fore.GREEN}data/{Fore.BLUE}urls-{spider.name}-{self.today}"
                           f"\n{Fore.RED} > {Fore.GREEN}data/{Fore.BLUE}stats-{spider.name}-{self.today} {Style.RESET_ALL}")

        
        file=f"data/stats-{spider.name}-{self.today}.json"

        with open(file,'w',encoding='utf-8') as f:
            
            json.dump(stats,f,ensure_ascii=False,indent=4,default=str)
                                                          #Object of type datetime is not JSON serializable
                                                          #default=str converts any non-serializable object to string automatically
    
    
    
    