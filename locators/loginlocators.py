from selenium.webdriver.common.by import By


class loginLocators(object):
    username = (By.ID, 'user-name')
    password = (By.ID, 'password')
    login_btn = (By.ID, "login-button")
    error_message = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3')