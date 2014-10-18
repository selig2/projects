import urllib, re
from createGmailMessage import *



def pollenReport():
	htmlfile = urllib.urlopen("http://www.wunderground.com/DisplayPollen.asp?Zipcode=61853")
	htmltext = htmlfile.read()

	pollenType = '<h3>(.+?)</h3>'
	pollenLevel = '<p>(.+?)</p>'

	ptPattern = re.compile(pollenType)
	ptInstance = re.findall(ptPattern, htmltext)

	lvlPattern = re.compile(pollenLevel)
	lvlInstance = re.findall(lvlPattern, htmltext)

	pollens = ptInstance[0][30:]#this was what I wanted at the time of writing the code. They may change the page and then this wouldn't be right.
	score = lvlInstance[4]#this was what I wanted at the time of writing the code. They may change the page and then this wouldn't be right.

	subject = "Your Daily Pollen Update is Here."
	bodymsg = "Today's Pollen Level for Mahomet is: "  + score + '.\n\n' + "Major pollens today: " + pollens + \
			  "\n\nRead more about today's pollen here: " + 'http://www.wunderground.com/DisplayPollen.asp?Zipcode=61853' + \
			  '\n\nThis message was made by request via PollenAutoBot.\nHave a great day!'
	
	to = ['michael@selig.com', 'selig2@illinois.edu']
	for address in to:
		createMessage(address, 'pollenautobot@gmail.com', 'skytower', subject, bodymsg)
	return "Message sent successfully."


pollenReport()