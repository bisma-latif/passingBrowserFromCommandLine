import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonSearch(unittest.TestCase):
    url = "http://automationpractice.com/index.php"

    def setUp(self):
        self.driver = webdriver.Chrome("drivers/chromedriver/chromedriver.exe")
        self.driver.get(self.url)

    def test_first(self):
        driver = self.driver
        driver.maximize_window()
        assert self.url in driver.current_url
        driver.set_page_load_timeout(30)
        self.assertIn("My Store", driver.title)
        elem = driver.find_element(By.NAME, "search_query")
        elem.send_keys("dress")
        driver.find_element(By.NAME, "submit_search").click()
        assert "Search" in driver.title
        elem = driver.find_element(By.NAME, "search_query")
        elem.send_keys("Maria")
        elem.send_keys(Keys.PAGE_UP)
        elem.clear()
        women_menu = driver.find_element(By.CSS_SELECTOR, "a[title=Women]")
        print(women_menu.is_displayed())
        print(elem.is_enabled())
        print(women_menu.is_selected())
        assert "WOMEN" in women_menu.text
        cart = driver.find_element(By.CSS_SELECTOR, "div[class=shopping_cart] > a")
        assert cart.value_of_css_property('title') in "View my shopping cart"
        print(women_menu.get_attribute('href'))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()



