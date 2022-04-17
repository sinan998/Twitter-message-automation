from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from hbilgi import kullaniciadi,sifre



url="https://twitter.com/i/flow/login"
dr=webdriver.Chrome("webdriver chrome adress (C:/Users/sinan/Desktop/chromedriver.exe)")
dr.get(url)
time.sleep(2)
dr.maximize_window()
time.sleep(2)

ka=dr.find_element_by_xpath("//input[@autocomplete='username']")
ka.send_keys("your username")
time.sleep(2)
ka.send_keys(Keys.ENTER)
time.sleep(2)

ks=dr.find_element_by_xpath("//input[@autocomplete='current-password']")
ks.send_keys("your password")
time.sleep(2)
ks.send_keys(Keys.ENTER)
time.sleep(3)

kisi="Username"
url="https://twitter.com/{}".format(kisi)
dr.get(url)
time.sleep(2)

mesajtık=dr.find_element_by_xpath("//div[@data-testid='sendDMFromProfile']")
time.sleep(2)
mesajtık.click()
time.sleep(2)

mesajsend=dr.find_element_by_xpath("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
mesajsend.send_keys("your message")
time.sleep(1)
mesajsend.send_keys(Keys.ENTER)

