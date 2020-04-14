from selenium import webdriver
from common.readconf import *
import time

def setup():
    url = ReadConf().get_login_url()
    driver = webdriver.Chrome(executable_path= 'C:\\Users\Administrator\AppData\Local\Programs\Python\Python37\chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    return driver


