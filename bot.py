from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from authdata import username, password, hashtag
import time
import random

class Instagrambot():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Firefox()

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self):
        browser = self.browser
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
        time.sleep(5)

    def hashtag_like (self):
                browser = self.browser
                browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
                time.sleep(6)
                for i in range(1,4):
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.randrange(3,5))

                hrefs = browser.find_elements(By.TAG_NAME,"a")
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
                        self.close_browser()
    #проверяем существует ли элемент на странице
    def xpath_exists(self, url):
        browser = self.browser
        try:
            browser.find_element(By.XPATH, url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist
    #ставим лайк на пост по прямой ссылке
    def put_like_post(self, userpost):
        browser = self.browser
        browser.get(userpost)
        time.sleep(4)

        wrong_userpage = '/html/body/div[1]/section/main/div/div/h2'
        if self.xpath_exists(wrong_userpage):
            print("Такой страницы не существует")
            self.close_browser()
        else:
            print("Пост успешно найден, ставим лайк!")
            time.sleep(2)

            like_button = "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button"
            browser.find_element(By.XPATH,like_button).click()

            print(f"лайк на пост: {userpost} поставлен")
            self.close_browser()

    def put_many_likes(self, userpage):

        browser = self.browser
        browser.get(userpage)
        time.sleep(5)
        wrong_userpage = '/html/body/div[1]/section/main/div/div/h2'
        if self.xpath_exists(wrong_userpage):
            print("Такой страницы не существует")
            self.close_browser()
        else:
            print("Пост успешно найден, ставим лайк!")
            time.sleep(2)

            post_count = int(browser.find_element(By.XPATH,"//section/main/div/header/section/ul/li[1]/div/span").text)
            loops_count = int(post_count / 12)
            if loops_count > 4:
                loops_count = 4

            print(loops_count)
            for i in range(0, loops_count):
                hrefs = browser.find_elements(By.TAG_NAME, "a")
                hrefs = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

                post_urls = []
                for href in hrefs:
                    post_urls.append(href)

                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))
                print(f"итерация #{i}")
            file_name = userpage.split("/")[-2]

            with open(f'{file_name}.txt', 'a') as file:
                for post_url in post_urls:
                    file.write(post_url + "\n")

            self.close_browser()

            # like_button = "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button"
            # browser.find_element(By.XPATH, like_button).click()
            # print(f"лайк на пост: {userpost} поставлен")

bot = Instagrambot(username,password)
bot.login()
#bot.put_like_post("https://www.instagram.com/p/CZmuqx0jAwf/")
bot.put_many_likes("https://www.instagram.com/beauty_room_tz/")


