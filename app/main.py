from glob import has_magic
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import track
import json


def main():
    # driver = webdriver.Remote('http://selenium:4444/wd/hub',
    #                           options=webdriver.ChromeOptions())

    username = ''
    username = username.replace('@', '')
    info = {
        'username': username
    }
    driver = webdriver.Chrome()
    has_ring = track.has_ring(username, driver)
    info.update(has_ring)
    has_mention = track.find_by_mention(username, driver)
    info.update(has_mention)
    driver.close()
    r = json.dumps(info)
    print(r)
    exit()


main()
