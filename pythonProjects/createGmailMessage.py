import smtplib, socket, sys, getpass

def createMessage(to, sender, password, subject, bodymsg):

    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)#URL and port number for smtp  #25 or 587(port#) worked for me as of 8/11/14 
    smtpserver.ehlo()#?
    smtpserver.starttls()#?
    smtpserver.ehlo()#?

    
    try:
        smtpserver.login(sender, password)
        
    except smtplib.SMTPExcpetion:
        
        print "Authentication Failure" + " \n most likely wrong password"
    
    header = 'To:' + to + "\n" + "From: " + sender + "\n" + "Subject: " + subject + "\n"

    msg = header + "\n" + bodymsg + "\n\n"

    smtpserver.sendmail(sender, to, msg)
    smtpserver.close()


#createMessage("colts8729@gmail.com", "crazycatfactshaha@gmail.com", "skytower")