import scrapy
import time
import urllib
import urllib2
import json

#Worked with Xi Chen, Bowei Zhang

url = 'http://localhost:8888/crawlerdb.db/TestTable2/'

from tutorial.items import myitem
class myspider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["https://leetcode.com/"]
    start_urls = [
        "https://leetcode.com/problemset/algorithms/"
	]

    def parse(self, response):
         for sel in response.xpath('//tr/td'):
            item = myitem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            
            ## print and sleep 2 second
            print "tilte = " , sel.xpath('a/text()').extract()
            print "link = ", sel.xpath('a/@href').extract()
            print "desc = ", sel.xpath('text()').extract()
            time.sleep(2)
            
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

#ur/li