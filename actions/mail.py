import yagmail

receiver = "pratikshashetty5618@gmail.com"
body = "Hello there, This Mail is From Python"
filename = "mail.py"

yag = yagmail.SMTP("altafshaikh123456789@gmail.com")
yag.send(
    to=receiver,
    subject="Python Mail Code",
    contents=body,
    attachments=filename, 
    
)
