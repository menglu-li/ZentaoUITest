import unittest
from common.setup import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginSuccess(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = setup()

    def tearDown(self) -> None:
        self.driver.close()

    def test_case_01(self):
        '''验证admin正确的用户名密码登录'''
        self.driver.find_element(By.ID, 'account').send_keys('admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123456')
        self.driver.find_element(By.ID, 'submit').click()
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH, '//span[@class="user-name"]'), 'admin')
        print('success test_case_01')

    def test_case_02(self):
        '''验证test01正确的用户名密码登录'''
        self.driver.find_element(By.ID, 'account').send_keys('test01')
        self.driver.find_element(By.NAME, 'password').send_keys('test123456')
        self.driver.find_element(By.ID, 'submit').click()
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH, '//span[@class="user-name"]'), 'admin')
        print('success test_case_02')

    def test_case_03(self):
        '''验证dev01正确的用户名密码登录'''
        self.driver.find_element(By.ID, 'account').send_keys('dev01')
        self.driver.find_element(By.NAME, 'password').send_keys('dev123456')
        self.driver.find_element(By.ID, 'submit').click()
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH, '//span[@class="user-name"]'), 'dev01')
        print('success test_case_03')

if __name__ =='__main__':
    unittest.main()

