import smtplib, socket, sys, getpass
from createGmailMessage import *
#good to go.

def massMail():#program run time: roughly O(N) 1 second for each address in textfile
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587)#use port 587
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	sender = "colts8729@gmail.com"#netID@illinois.edu, or username@gmail.com ONLY
	password = "col18gma"
	try:
		smtpserver.login(sender, password)

	except smtplib.SMTPException:
		print "Authentication Failure" + " \n" + "most likely wrong password."

	addressFile = open("addresses.txt") #open text file containing list of addresses
	addressList = addressFile.read()
	addressList = addressList.split("\n")


	subject = "TestRun"#insert subject here
	bodymsg = "Hi FSONE\n new update is here!"#insert bodymessage here

	for address in addressList:
		to = address.strip()
		header = 'To:' + to + "\n" + "From: " + sender + "\n" + "Subject: " + subject + "\n"
		msg = header + "\n" + bodymsg + "\n\n"
		
		smtpserver.sendmail(sender, to, msg)
		print "Message was sent to: " + to + "\n"
		#pause = raw_input("Press ENTER to continue")

	return "All messages were sent successfully. \n\nProgram closing now."

	smtpserver.close()
	

massMail()