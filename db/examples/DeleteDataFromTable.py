import urllib2
import json

url = 'http://localhost:8888/crawlerdb.db/TestTable/2'			# set the url of the database and table to fetch from; here
																		#'crawlerdb.db' is the database and 'TestTable' is the table name
																		# 2 is the primary key of the row to delete
opener = urllib2.build_opener(urllib2.HTTPHandler)				# open a HTTPHandler
request = urllib2.Request(url)										# create a request object
request.get_method = lambda: 'DELETE'							# set HTTP method type to DELETE
opener.open(request)												# send request to delete row with primary key '2'