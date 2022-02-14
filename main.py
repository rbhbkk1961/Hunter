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
        # time.sleep(10)
        # curent_url = browser.current_url
        # print(curent_url)
        # if curent_url == 'https://www.instagram.com/accounts/onetap/?next=%2F':
        #     save_button = browser.find_elements(By.TAG_NAME,"button")
        #     save_button.select_by_visible_text("Сохранить данные")
        # else: pass

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

login(username,password)