import urllib
from datetime import datetime
from createGmailMessage import *
###################################requires user to have a blank.txt file and hrvLog.txt file in the same directory
################ as this program
########################### also copy paste: Opened 2014-08-13 19:04:21.433000 19 into first line of hrvLog.txt and hit enter and save.

configFile = open('/home/selignet/pythonProjects/configFile.txt', 'r')
configTxt  = configFile.read().strip('\n')

dewPtLimit   = configTxt[0][0:2]  # the second position "2" is non-inclusive (oddly)
dewPtDiff    = configTxt[1][0:1]
relHumdLimit = configTxt[2][0:2]


configFile.close()

def hrvFunction():
	try:
		htmlfile = urllib.urlopen("http://www.atmos.illinois.edu/weather/")
		htmltext = htmlfile.read()
	except:
		return "hrvbot@gmail.com cannot currently connect to: " + "http://www.atmos.illinois.edu/weather/"

	target = open('/home/selignet/pythonProjects/blank.txt', 'w')
	target.write(htmltext)
	target.close()

	sourceCode = open("/home/selignet/pythonProjects/blank.txt", 'r')
	for line in sourceCode:
		if("Temperature:" in line):
			temp = line

		if("Rel. Humidity:" in line): 
			relHumd = line
		if("Dew Point:" in line):
			dewPt = line

	temp = int(temp[24:26])
	relHumd = int(relHumd[19:21])
	dewPt =int(dewPt[15:17])
	return [temp, relHumd, dewPt]

def autoCheck():

	print "================================================="

	currentHour = datetime.now().hour
	currentHour = int(currentHour)
	dateTime = datetime.now()


	temp = hrvFunction()[0]
	relHumd = hrvFunction()[1]
	dewPt = hrvFunction()[2]

	readLog = open("/home/selignet/pythonProjects/hrvLog.txt")
	logList = readLog.readlines()
	lastHour = int(logList[len(logList) - 1][34:])
	lastState = logList[len(logList) - 1][:6]
	

	writeHRVLog = open("/home/selignet/pythonProjects/hrvLog.txt", 'a')

	#shouldBeClosed = (dewPt > int(dewPtLimit) and (temp - dewPt) < int(dewPtDiff) and relHumd > int(relHumdLimit))
	shouldBeClosed = ( dewPt > 53 and (temp - dewPt) < 5 and relHumd > 80 )

	# shouldBeClosed = True

	# -----------------------------
	# reporting
	if( shouldBeClosed ):
		print "Should be closed."
	else:
		print "Should be open."

	print "This is the current hour: " + str(currentHour)
	# -----------------------------


	shouldBeOpen = not shouldBeClosed

	if(lastState == "Opened" and shouldBeClosed):

		bodymsg = "These stats have caused a trigger to remind you to close the HRV: \n\n"  + "Temperature: " + str(temp) + " degrees." "\n" + "Relative Humidity: " + str(relHumd) + \
				  	 "%" + "\n" + "Dew Point: " + str(dewPt) + " degrees." + "\n\n"
		subject = "Close HRV."
		log = ['Closed', ' ', str(dateTime), ' ', str(currentHour), '\n']

		writeHRVLog.writelines(log)
		writeHRVLog.close()

		createMessage("michael@selig.com", "hrvbot@gmail.com", "skytower", subject, bodymsg)
		print "Sending email to michael@selig.com to remind to close HRV"
		

	elif(currentHour >= (lastHour + 10) % 12 and lastState == "Closed" and shouldBeOpen): #and shouldclose
		bodymsg = "These stats have caused a trigger to remind you to open the HRV: \n\n" "Temperature: " + str(temp) + " degrees." "\n" + "Relative Humidity: " + str(relHumd) + \
				  	 "%" + "\n" + "Dew Point: " + str(dewPt) + " degrees." + "\n\n"
		subject = "Open HRV."
		log = ['Opened', ' ', str(dateTime), ' ', str(currentHour), '\n']

		writeHRVLog.writelines(log)
		writeHRVLog.close()


		createMessage("michael@selig.com", "hrvbot@gmail.com", "skytower", subject, bodymsg)
		print "Sending email to michael@selig.com to remind to turn on HRV"


	print "================================================="


	
	
	readLog.close()
	#add reminder after 10 hours

	
autoCheck()
