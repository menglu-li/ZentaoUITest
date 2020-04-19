from selenium import webdriver
from common.readconf import *
import time, os

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')

def setup():
    url = ReadConf().get_login_url()
    driver = webdriver.Chrome(executable_path= driver_path)
    # driver = webdriver.Chrome(executable_path= 'C:\\Users\Administrator\AppData\Local\Programs\Python\Python36\Scripts\chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    return driver

