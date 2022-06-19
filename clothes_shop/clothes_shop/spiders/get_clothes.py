import scrapy


class GetClothesSpider(scrapy.Spider):
    name = 'get_clothes'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['scrapingclub.com/exercise/list_basic/']

    def parse(self, response):
        pass
    
