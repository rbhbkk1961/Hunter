from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from authdata import username, password
#import fake_useragent from User

def login(username,password):
    try:
        #options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox()
        browser.get('https://instagram.com')
        time.sleep(random.randrange(3,5))
        username_input = browser.find_element(By.NAME,"username")
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(2)
        # пароль
        password_input = browser.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

login(username,password)