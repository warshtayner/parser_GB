from turtle import title
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GetClothesCrawlSpider(CrawlSpider):
    name = 'get_clothes_crawl'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['http://scrapingclub.com/exercise/list_basic/']

    rules = (
        # Rule(LinkExtractor(restrict_xpaths="//a[contains(text(), 'Next')]"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//h4[@class='card-title']/a"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = {
            'name' : response.xpath("//div[@class='card-body']/h3/text()").get(),
            'price': response.xpath("//div[@class='card-body']/h4/text()").get(),
            'description' : response.xpath("//div[@class='card-body']/p/text()").get(),
            'img' : "https://scrapingclub.com/" + response.xpath("//img[@class='card-img-top img-fluid']/@srg").get()
        }

        return item
