import urllib, re
from createGmailMessage import *


def weatherReport():
	htmlfile = urllib.urlopen('http://www.weather.com/weather/today/Mahomet+IL+61853:4:US')
	htmltext = htmlfile.read()

	rnTemp =  '<span itemprop="temperature-fahrenheit">(.+?)</span>'
	conditions = '<div class="wx-phrase ">(.+?)</div>'
	tonightTemp = '<div class="wx-temperature">(.+?)</div>'

	rntPattern = re.compile(rnTemp)
	conditionsPattern = re.compile(conditions)
	tonightTempPattern = re.compile(tonightTemp)


	rntInstance = re.findall(rntPattern, htmltext)
	conditionsInstance = re.findall(conditionsPattern, htmltext)
	tonightTempInstance = re.findall(tonightTempPattern, htmltext)

	
	currentConditions = conditionsInstance[0]
	tonightConditions = conditionsInstance[2]
	currentTemp  = rntInstance[0]
	tonightTemp = tonightTempInstance[2][:2]
	print currentTemp

	to = ['colts8729@gmail.com', 'lisa@selig.com']
	sender = 'weather.bot1'
	subject = 'Your Daily Weather Forecast is Here'
	bodymsg = "Right now: " + currentTemp +' degrees.' + '  '  + currentConditions + '.' + "\n"  +"Tonight: "  + \
			   tonightTemp + ' degrees.' + '  ' + tonightConditions + '.\n\n' + "Read more about today's weather here: "\
			   "http://www.weather.com/weather/today/Mahomet+IL+61853:4:US" + "\n"  + "This message was mad by request via WeatherBot.\nHave a great day."

	for address in to:
		createMessage(address, 'weather.bot1@gmail.com', 'skytower', subject, bodymsg)

	return


weatherReport()


