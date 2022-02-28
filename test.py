from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from authdata import username, password, hashtag
import time
import random
import requests
browser = webdriver.Firefox()
browser.get('https://instagram.com')
time.sleep(random.randrange(8, 10))
username_input = browser.find_element(By.NAME, "username")
username_input.clear()
username_input.send_keys(username)
time.sleep(3)
        # пароль
password_input = browser.find_element(By.NAME, "password")
password_input.clear()
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)
time.sleep(6)

url = "https://www.instagram.com/p/CQOUfKqh_y-/"
try:
    browser.get(url)
    p=browser.find_element(By.XPATH, url)
    print(p)
except Exception as ex:
    print(ex)
