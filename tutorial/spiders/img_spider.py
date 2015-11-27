import scrapy

# before running this spider, install
# sudo apt-get install libjpeg-dev
# sudo easy_install pillow

# this can be run on command line by
#  scrapy crawl imgspider -a start_urls=http://blog.flickr.net/en/2013/12/18/flickr-web-embeds/ -a domain=flickr.net -s IMAGES_STORE=/home/rajat/images/ -s DEPTH_LIMIT=1 -s DOWNLOAD_DELAY=2

from scrapy.contrib.spiders import Rule, CrawlSpider
from tutorial.items import ImgItem

class ImgSpider(CrawlSpider):
	name = 'imgspider'
	
	def __init__(self, domain=None, start_urls=[]):
		self.allowed_domains = domain
		self.start_urls = start_urls.split(',')

	def parse(self, response):
		for sel in response.xpath("//img/@src"):
			image = ImgItem()
			image['title'] = sel.extract()
			image['image_urls'] = [sel.extract()]
			yield image