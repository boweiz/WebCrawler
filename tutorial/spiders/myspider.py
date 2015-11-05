import scrapy
from tutorial.items import myitem
class myspider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["http://www.cmu.edu/"]
    start_urls = [
        "http://www.cmu.edu/research/"
	]

    def parse(self, response):
         for sel in response.xpath('//ul/li'):
            item = myitem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
