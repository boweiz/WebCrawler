import scrapy

import urllib
import urllib2
import json

url = 'http://localhost:8888/crawlerdb.db/TestTable2/'

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
	    
	    ##### This part is for inserting into DB #####
	    title = item['title'][0] if item['title'] else None
	    link = item['link'][0] if item['link'] else None
	    desc = item['desc'][0] if item['desc'] else None
	    params = urllib.urlencode({
		'title' : title,
		'link' : link,
		'desc' : desc
	    })
	    response = urllib2.urlopen(url, params).read()
	    ##### End of insertion into DB #####

            yield item
