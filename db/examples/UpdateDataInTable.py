import urllib
import urllib2
import json

url = 'http://localhost:8888/crawlerdb.db/TestTable/1'			# set the url of the database and table to update; here
																		#'crawlerdb.db' is the database and 'TestTable' is the table name
																		# 1 is the primary ID of the row to update

params = urllib.urlencode({											# build a list of json parameters
	'RandomString' : 'Kapoor'										# here we are updating the 'RandomString' column for Primary key '1' in TestTable
})

urllib2.urlopen(url, params).read()									# send the update request