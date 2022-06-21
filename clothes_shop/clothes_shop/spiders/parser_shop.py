import scrapy


class ParserShopSpider(scrapy.Spider):
    name = 'parser_shop'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    def parse(self, response):
        all_clothes = response.xpath("//div[@class='col-lg-4 col-md-6 mb-4']")
        for clothe in all_clothes:
            yield {
                'name' : clothe.xpath(".//h4[@class='card-title']/a/text()").get(),
                'price': clothe.xpath(".//div[@class='card']/h5/text()").get(),
                'img' : response.urljoin(clothe.xpath(".//div[@class='card']/a/img/@src").get())
            }
        
        next_page = response.xpath("//a[contains(text(), 'Next')]/@href").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

