######### automate tinder so that you don't need to login ##########################
from selenium import webdriver

#### activate headlesss mode so browser does not have to open when extracting data ####
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##exceptions: used if we DO NOT find element from website
from selenium.common.exceptions import NoSuchElementException
import time
from random import randint


website = "https://www.tinder.com"

##path containing chrome driver
path = "/Users/awadsharif/Downloads/chromedriver_mac64/chromedriver"

number_of_swipes = 100

##message
opening_line = "Hi!"

##headless mode
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
service = Service(executable_path=path)

##set options equal to options to make it headless
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
##maximize window
driver.maximize_window()

##xpath for like button
#//button[@data-testid="gamepadLike"]

##need about 10 seconds to load up all the cards
time.sleep(10)
##click on like button as many times as we want
for i in range(number_of_swipes):
    ##use try except block
    try:
        like_button = driver.find_element(by='xpath', value='//button[@data-testid="gamepadLike"]')
        #like_button.click()
        ##NOTE: for clicking like button better to use following format:
        driver.execute_script("arguments[0].click();", like_button)
        time.sleep(1)
 
    ##encounter "Upgrade Your Like" icon
    ##find window parent where "no thanks" button belongs too, use span and text to obtain "No thanks"
    ##//div[@data-testid="dialog"]
    ##Get the span "No Thanks" button from the div containing "No Thanks" button.
    ##text attribute is invisible, not visible on element itself,
    ##//div[@data-testid="dialog"]//span[text()=


    ##when we get IT"S A MATCH window, send message that is auto-sent.
    ##select the textarea
    #//textarea[@placeholder="Say something nice"]
        its_match_window = driver.find_element(by='xpath', value='//textarea[@placeholder="Say something nice"]')
        #message to send in textbox
        its_match_window.keys(opening_line)
        time.sleep(1)

        ##automate send button
        send_message_button = driver.find_element(by="xpath", value='//button[@data-testid="chatSendMessageButton"]')
        time.sleep(1)
        #click on send message button
        send_message_button.click()

        #close button to close the "It's a match!" window
        close_its_match_window = driver.find_element(by="xpath", value='//button[@title="Back to Tinder"]')
        close_its_match_window.click()

##exceptions: used if we DO NOT find element from website, find popups
    except NoSuchElementException:
        try:
        # find EITHER of these buttons in any popup windows, write it this way b/c they ALL occur during popups.
            box = driver.find_element(by="xpath", value=' //div[@data-testid="dialog"]//span[text()="No Thanks"] | //div[@data-testid="dialog"]//span[text()="Not interested"] | //div[@data-testid="dialog"]//span[text()="Maybe Later"]')
            box.click()
        ##used if NO popups are found
        except NoSuchElementException:
            pass






##### Buttons for popups that arise on Tinder #####


##//div[@data-testid="dialog"]//span[text()="No Thanks"]
##//div[@data-testid="dialog"]//span[text()="Not interested"]
##//div[@data-testid="dialog"]//span[text()="Maybe Later"]