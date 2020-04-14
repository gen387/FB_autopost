from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import random
import time

#opening browser
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("/Users/er/Boty/PyBot FB/chromedriver", options=chrome_options)
driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("Opened facebook...")

#passing login and password
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
#                   email address here
email.send_keys('email_address@mail.com')
#                   email address here
print("Email Id entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
#                   password here
password.send_keys('password')
#                   password here
print("Password entered...")

#logging in & delay 5s
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
time.sleep(2)
print("FB opened")

#posting with XXs delay
filePath = '/Users/er/Boty/PyBot FB/links/links.txt'
with open(filePath) as readFile:
    for cnt, line in enumerate(readFile):
        driver.get("https://www.facebook.com")
        statusBox= driver.find_element_by_xpath("//*[@name='xhpc_message']")
        statusBox.click()
        newStatus = "{}".format(line)
        statusBox.send_keys(newStatus)
        time.sleep(2)
        postbutton = driver.find_element_by_xpath("//button[contains(.,'Opublikuj')]")
        time.sleep(random.randrange(60, 120, 1))
        postbutton.click()
        time.sleep(60)
        print("posting", "{}".format(line), "done")
