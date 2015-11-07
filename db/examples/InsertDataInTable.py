import urllib
import urllib2
import json

url = 'http://localhost:8888/crawlerdb.db/TestTable/'				# set the url of the database and table to update; here
																		#'crawlerdb.db' is the database and 'TestTable' is the table name

params = urllib.urlencode({											# build a list of json parameters
	'RandomString' : 'Rajat'											# here we are inserting a value in 'RandomString' column
})																		# we haven't provided a value for 'ID_PRIMARY' column because it is AUTO_INCREMENTING

response = urllib2.urlopen(url, params).read()						# send the insert request
print response