from selenium import webdriver
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import json
import random
config = json.loads(open("./config.json").read())
instaDirectory = config["instaDirectory"]
os.environ["INSTA_BOT"] = instaDirectory
os.chdir(os.environ["INSTA_BOT"])
link = 'https://instagram.com'
hastags = ['memes', 'fun', 'adventure']

class InstagramBot:
    service = Service('/usr/local/bin/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)
    username = config["username"]
    password = config["password"]

    def __init__(self):
        driver = self.driver
        username = self.username
        password = self.password
        driver.get(link)
        sleep(3)
        try:
            driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        except:
            sleep(2)
            driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
            driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(password)
            driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            sleep(4)
        try:
            driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
        except Exception:
            sleep(2)

    def newFollows(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//a[contains(text(), 'See All')]")\
            .click()
        except:
            driver.get("https://www.instagram.com/explore/")
            driver.find_element_by_xpath("//a[contains(text(), 'See All')]")\
                .click()

        for i in range(1, 3):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # Getting all the button with Follow text
                try:
                    buttons = driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
                    for btn in buttons:
                        # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
                        driver.execute_script("arguments[0].click();", btn)
                        time.sleep(random.randint(2, 10))
                except:
                    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                        .click()
            except Exception:
                continue
        driver.quit()

    def newFollowswithphotos(self):
        driver = self.driver
        try:
            liked_by_button = lambda: driver.find_element_by_xpath('//button[@class="sqdOP yWX7d     _8A5w5    "]')
            liked_by_button().click()
        except Exception:
            driver.get("https://www.instagram.com/explore/")
            driver.find_element_by_xpath("//a[contains(text(), 'See All')]")\
                .click()
        try:
            buttons = driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
            for btn in buttons:
                # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(random.randint(2, 10))
        except:
            driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]")\
                .click()
        driver.quit()

    def newLikesAndComments(self):
        driver = self.driver
        while True:
            try:
                search = random.choice(hastags)
                driver.get("https://www.instagram.com/explore/tags/" + search + "/")
                time.sleep(2)
                pic_hrefs = []
                for i in range(1, 2):
                    try:
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(2)
                        # getting all the tags
                        hrefs_in_view = driver.find_elements_by_tag_name('a')
                        # finding all the hrefs
                        hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                         if '.com/p/' in elem.get_attribute('href')]
                        # building the list of photos
                        [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                    except Exception:
                        continue

                # Click on Like Button
                unique_photos = len(pic_hrefs)
                comments = ['Nice picture I love it', 'I love this', '😍', 'Good Stuff', 'Keep it up!', 'Class!']

                for pic_href in pic_hrefs:
                    driver.get(pic_href)
                    time.sleep(4)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    try:
                        time.sleep(random.randint(2, 4))
                        # Hit Like
                        liked_by_button = lambda: driver.find_element_by_xpath('//button[@class="wpO6b "]')
                        liked_by_button().click()
                        time.sleep(random.uniform(2, 4))
                        comment_btn = lambda: driver.find_element_by_tag_name('textarea')
                        comment_btn().click()
                        comment_btn().clear()
                        time.sleep(random.uniform(2, 4))
                        comment = random.choice(comments)
                        for letter in comment:
                            comment_btn().send_keys(letter)
                            time.sleep(random.randint(1,9)/10)
                        comment_btn().send_keys(Keys.RETURN)
                        # Close Image
                        driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
                        time.sleep(1)
                    except Exception as e:
                        time.sleep(2)
                    unique_photos -= 1
                driver.quit()
            except Exception:
                time.sleep(60)
                driver.quit()

    def newUnfollow(self):
        driver = self.driver
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        for i in range(1, 2):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # Getting all the button with Follow text
                try:
                    buttons = driver.find_elements_by_xpath("//button[contains(.,'Following')]")
                    for btn in buttons:
                        # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
                        driver.execute_script("arguments[0].click();", btn)
                        time.sleep(random.randint(2, 4))
                        driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]")\
                        .click()
                except:
                    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                        .click()

            except Exception:
                continue
        driver.quit()

if __name__ == '__main__':
    Insta = InstagramBot()
    # Uncomment the function below that you want to run:
    #Insta.newFollows()
    #Insta.newFollowswithphotos
    Insta.newLikesAndComments()
    #Insta.newUnfollow()
