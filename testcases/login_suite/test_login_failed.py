import unittest
from webdriver.setup import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginFailed(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = setup()

    def tearDown(self) -> None:
        self.driver.close()

    def test_case_01(self):
        '''验证正确用户名+错误密码登录'''
        self.driver.find_element(By.ID, 'account').send_keys('admin')
        self.driver.find_element(By.NAME, 'password').send_keys('123456')
        self.driver.find_element(By.ID, 'submit').click()
        time.sleep(2)
        self.assertTrue(EC.alert_is_present()(self.driver))
        print('failed test_case_01')

    def test_case_02(self):
        '''验证错误用户名+错误密码登录'''
        self.driver.find_element(By.ID, 'account').send_keys('test')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123456')
        self.driver.find_element(By.ID, 'submit').click()
        time.sleep(2)
        self.assertTrue(EC.alert_is_present()(self.driver))
        print('failed test_case_02')

if __name__ == '__main__':
    unittest.main()




