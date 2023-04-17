from selenium.webdriver.common.by import By
from Tests.base_test import BaseTest
from data import userdetails
from data import messages
from locators import loginlocators


class Test_SauceDemo(BaseTest):

    def test_the_user_can_login_successfully(self):
        driver = self.driver
        username = driver.find_element(*loginlocators.loginLocators.username)
        username.send_keys(userdetails.username)
        password = driver.find_element(*loginlocators.loginLocators.password)
        password.send_keys(userdetails.password)
        driver.find_element(*loginlocators.loginLocators.login_btn).click()
        assert "/inventory.html" in driver.current_url

    def test_the_user_can_enters_incorrect_password(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        username = driver.find_element(*loginlocators.loginLocators.username)
        username.send_keys(userdetails.username)
        password = driver.find_element(*loginlocators.loginLocators.password)
        password.send_keys(userdetails.incorrect_password)
        driver.find_element(*loginlocators.loginLocators.login_btn).click()
        error_msg = driver.find_element(*loginlocators.loginLocators.error_message)
        assert messages.expected_text == error_msg.text
