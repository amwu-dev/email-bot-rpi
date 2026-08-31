# Import smtplib for the actual sending function
import smtplib #anki
import secrets
import random
import time
import glob
# Import the email modules we'll need
from email.message import EmailMessage #anki

# Open the plain text file whose name is in textfile for reading.
msg = EmailMessage()
msg.set_content("Good Morning!")

# me == the sender's email address
# you == the recipient's email address


msg['Subject'] = f'From William <3'
msg['From'] = secrets.sender
msg['To'] = secrets.recepient

images = glob.glob('images/*.png') #anki
for file in images:
    with open(file, 'rb') as fp:
        img_data = fp.read()
    msg.add_attachment(img_data, maintype='image',
                                 subtype='png',filename=file.split('/')[-1])
    
# Send the message via our own SMTP server.
# send it within 10 minutes
random.seed()

sleep_time = random.randint(0, 600) #anki
print("Sleeping for " + str(sleep_time) + " seconds before sending the message...")
time.sleep(sleep_time) #anki
print("Sending message...")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server: 
    smtp_server.login(secrets.sender, secrets.password)
    smtp_server.sendmail(secrets.sender, secrets.recepient, msg.as_string())
    print("Message sent!")
