import scrapy

from tutorial.items import TutorialItem

class myspider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["http://www.awwwards.com/"]
    start_urls = [
                  "http://www.awwwards.com/search-websites/?text=game&submit=OK/"
                  ]
                  
    def parse(self, response):
        for sel in response.xpath('//h3'):
            item = TutorialItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item