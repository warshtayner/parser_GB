import scrapy


class ScrapySplashSpider(scrapy.Spider):
    name = 'scrapy_splash'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/detail_sign/']

    def parse(self, response):
        yield {
            'title': response.xpath("//h4[@class='card-title']").get(),
            'price': response.xpath("//h4[@class='card-price']").get(),
            'description': response.xpath("//p[@class='card-description']").get(),
            'img': response.urljoin((response.xpath("//img[contains(@class, 'card-img-top')]/@src").get()))
        }
