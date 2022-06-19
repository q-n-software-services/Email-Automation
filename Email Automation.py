import requests
from bs4 import BeautifulSoup

# send the email
import smtplib

# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

# email content placeholder

content = ''

# extracting Hacker News stories

def extract_news(url):
    print('Extracting Hacker News Stories....')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text != 'More' else '')

    return cnt

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

# print(content)

# lets send the email

print('Composing Email....')

# Update your Email Details

SERVER = 'smtp.gmail.com' # your smtp server
PORT = 587 # your Port Number
FROM = 'muhammadmohib3@gmail.com' # "Your From Email ID"
TO = ['muhammadmohib1227292@gmail.com', 'tayyabsenate@gmail.com'] # "Your To Email Ids " Can be a list
PASS = '$mohib$122' # "Your Email Id's Password


# Create a text/plain message

msg = MIMEMultipart()

msg.add_header('Content-Disposition', 'attachment', filename='HongKong project.py')

msg['Subject'] = 'Top News Stories HN (Automated Email)' + '' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print("Initializing Server....")

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(0)
server.ehlo()
server.starttls()
server.login(FROM, PASS)

server.sendmail(FROM, TO, msg.as_string())

print('Email Sent !')

server.quit()



