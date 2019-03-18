import yagmail

def send_mail(to,msg,sub):
	receiver = to
	body = msg
	#filename = "mail.py"
	sender = "altafshaikh123456789@gmail.com"


	yag = yagmail.SMTP(sender)
	yag.send(
	    to=receiver,
	    subject=sub,
	    contents=body,
	    #attachments=filename,     
	)
