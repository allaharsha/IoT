import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "alert.yourhome@gmail.com"
toaddr = "alla.sriharsha94@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "For live, proceed to following link"
 
body = "https://www.youtube.com/channel/UCELoEYg2Jz63d-s7HFsewkg"
 
msg.attach(MIMEText(body, 'plain'))
 
filenames = ('/home/pi/project/image1.jpg','/home/pi/project/image2.jpg','/home/pi/project/image3.jpg','/home/pi/project/image4.jpg','/home/pi/project/image5.jpg')
for file in filenames:
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(file,'rb').read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % file)
 
	msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "4848026296")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
