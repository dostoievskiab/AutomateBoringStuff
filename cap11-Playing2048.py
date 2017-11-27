#This program plays the game 2048 terrible poorly (better than i)
#You will need to download the 'geckodriver' and copy it to /usr/local/bin/
#Im using 0.19.1 geckodriver version
#TOP SCORE is 3180 running for
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
browser = webdriver.Firefox()
browser.get('http://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

def randomKeys(x):
    return{
        1:htmlElem.send_keys(Keys.DOWN),
        2:htmlElem.send_keys(Keys.UP),
        3:htmlElem.send_keys(Keys.LEFT),
        4:htmlElem.send_keys(Keys.RIGHT),
    }[x]

while True:
    try:
        browser.find_element_by_class_name('game-over')
        btnRestart = browser.find_element_by_class_name('restart-button')
        btnRestart.click()
    except:
        randomKeys(random.randint(1,4))
