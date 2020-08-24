from time import sleep

import selenium
from selenium import webdriver
from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get('https://hao.360.com/')
    sleep(15)
