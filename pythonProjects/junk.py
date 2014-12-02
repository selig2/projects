import urllib, urllib2, time
from bs4 import BeautifulSoup
def postRequests(url, headers, payload, outFile):

	data = urllib.urlencode(payload) #encode the payload into a string
	req = urllib2.Request(url, data, headers) #make the request
	response = urllib2.urlopen(req) #get the response
	file = open(outFile, "w") #write the html to an html file
	the_page = response.read()
	print "Writing file... "
	time.sleep(1)
	print "3..."
	time.sleep(1)
	print "2..."
	time.sleep(1)
	print "1..."
	time.sleep(1)
	file.write(the_page)
	print "File Written. Exiting now."
	file.close()
	return the_page

URL = "http://www.teamrankings.com/ajax/league/v3/stats_controller.php"
payload = {"type": "team-detail", "league": "nfl", "stat_id": "4", "season_id": "12", "view": "stats_v1", "date": "11%2F30%2F2014"}
headers = {"X-Requested-With": "XMLHttpRequest"}

html = postRequests(URL, headers, payload, "ppp.html" )

def parseHTML():
	soup = BeautifulSoup(html)
	tableValues = soup.find_all("td")
	for value in tableValues:
		print value.get("rel")

print parseHTML()
