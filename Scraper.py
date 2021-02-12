import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/New-Apple-iPhone-Pro-512GB/dp/B08L5QN5MB/ref=sr_1_1_sspa?crid=1G05RYN194O2L&dchild=1&keywords=iphone+12+pro+max&qid=1613164880&sprefix=iphone+%2Caps%2C187&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4RkpIUjIyMThOQjUmZW5jcnlwdGVkSWQ9QTA1MzAyMzcxR09JREZSR0dBRUQ1JmVuY3J5cHRlZEFkSWQ9QTAyOTcyNzAyV1RHVURUVTIxTzdNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6].replace(",",""))

    if (converted_price > 1100):
        send_mail()
    
    print(converted_price)
    print(title.strip())



def send_mail():
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('EMAIL ADDRESS INSERT', 'PASSWORD INSERT')

    subject = 'Price of Iphone Fell on Amazon!'
    body = 'Check the amazon link https://www.amazon.co.uk/New-Apple-iPhone-Pro-512GB/dp/B08L5QN5MB/ref=sr_1_1_sspa?crid=1G05RYN194O2L&dchild=1&keywords=iphone+12+pro+max&qid=1613164880&sprefix=iphone+%2Caps%2C187&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4RkpIUjIyMThOQjUmZW5jcnlwdGVkSWQ9QTA1MzAyMzcxR09JREZSR0dBRUQ1JmVuY3J5cHRlZEFkSWQ9QTAyOTcyNzAyV1RHVURUVTIxTzdNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'EMAIL ADDRESS INSERT',
        'EMAIL SENDING TO INSERT',
        msg
    )

    print('The email has been sent')

    server.quit

while(True):
    check_price
    time.sleep(8640)
