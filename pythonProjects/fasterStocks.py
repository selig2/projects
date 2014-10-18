import urllib, re, json, time
def main():

	stocksFile = open('stocks.txt', 'r')
	stocks = stocksFile.read().split("\n")

	
	for stock in stocks:

		htmltext=  urllib.urlopen('http://www.bloomberg.com/markets/chart/data/1D/' + stock + ':US')#need a http:// before www.
	#because python needs to know the request. http is the request.
		
		data = json.load(htmltext)#json doesn't want a string, it wants a file. Aka don't use .read() because that makes it a string
	#json returns a hash map, or dictionary. If you want to access elements like a list give it the corresponding key not an index.
		x = data['data_values']

		if(x == []):
			print "Current price for: " + stock + "-- Null"
		else:	
			y = x[len(x) - 1][1]

		
		print 'Current price for: ' + stock + "-- $" +  str(y)



print main()