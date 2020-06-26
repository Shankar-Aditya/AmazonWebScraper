import requests
import bs4
import smtplib
import time


url='https://www.amazon.in/dp/B07PTLD8P9/ref=pc_mcnc_merchandised-search-16_?pf_rd_s=merchandised-search-16&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=VEJ4JP49815DTXG759AT&pf_rd_p=5855ae9b-f34e-4260-89c1-61eeae323329'
header={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


def check_price():
 page=requests.get(url,headers=header)
 soup= bs4.BeautifulSoup(page.content,'html.parser')
 title=soup.find(id="productTitle").get_text()
 price=soup.find(id="priceblock_ourprice").get_text()
 real_price1 = price[2:4]
 real_price2 = price[5:8]
 converted_price1 = float(real_price1)
 converted_price2 = float(real_price2)
 converted_price = (converted_price1 * 1000) + converted_price2
 print(title.strip())
 print(converted_price)
 if(converted_price<15000):
     send_mail()
 else:
     print('Too expensive')



def send_mail():
 server=smtplib.SMTP('smtp.gmail.com',587)
 server.ehlo()
 server.starttls()
 server.ehlo()
 server.login('#############','###########')     #Email and App Passsword to be entered.#
 subject='Price is down'
 body='Check link https://www.amazon.in/dp/B07PTLD8P9/ref=pc_mcnc_merchandised-search-16_?pf_rd_s=merchandised-search-16&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=VEJ4JP49815DTXG759AT&pf_rd_p=5855ae9b-f34e-4260-89c1-61eeae323329'
 msg=f"Subject:{subject}\n\n{body}"
 server.sendmail(
     '##############',          #Email of Sender#
     '##############',          #Email of Reciever#
     msg
 )
 print('Hey Email has been sent!')
 server.quit()

while True:
 check_price()
 time.sleep(20)       #This function puts the web scraper in a Sleep Mode for the time required#
