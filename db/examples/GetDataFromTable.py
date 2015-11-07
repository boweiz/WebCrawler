import urllib2
import json

url = 'http://localhost:8888/crawlerdb.db/TestTable/'				# set the url of the database and table to fetch from; here
																		#'crawlerdb.db' is the database and 'TestTable' is the table name
response = json.load(urllib2.urlopen(url))					# get all records from the table and load them into a
																#json object 'response'
for value in response:								# iterate over each row in the table
	print value['ID_PRIMARY']					# print value in column 'ID_PRIMARY'
	print value['RandomString']					# print value in column 'RandomString'

# If you want to fetch only one row from the table 'TestTable' and you know the 
# 'ID_PRIMARY' i.e. primary id which is 1 for e.g. , you can set url = 'http://localhost:8888/crawlerdb.db/TestTable/1'
# this will fetch only that particular row instead of all rows from the table
