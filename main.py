from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from authdata import username, password, hashtag
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

def hashtag_search(username,password,hashtag):
        try:
            # options = webdriver.FirefoxOptions()
            browser = webdriver.Firefox()
            browser.get('https://instagram.com')
            time.sleep(random.randrange(3, 5))
            username_input = browser.find_element(By.NAME, "username")
            username_input.clear()
            username_input.send_keys(username)
            time.sleep(2)
            # пароль
            password_input = browser.find_element(By.NAME, "password")
            password_input.clear()
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
            time.sleep(7)
            try:
                browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
                time.sleep(6)
                for i in range(1,4):
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.randrange(3,5))

                hrefs = browser.find_elements(By.TAG_NAME,"a")
                # post_urls = []
                # for item in hrefs:
                #     href = item.get_attribute('href')
                #     if "/p/" in href:
                #         post_urls.append(href)
                #     print(href)
                post_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
                for url in post_urls[0:1]:
                    try:
                        browser.get(url)
                        time.sleep(6)
                        like_button = browser.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
                        like_button.click()
                        time.sleep(random.randrange(80,100))
                    except Exception as ex:
                        print(ex)
            except Exception as ex:
                print(ex)
                browser.close()
                browser.quit()
        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

#login(username,password)

hashtag_search(username,password,hashtag)