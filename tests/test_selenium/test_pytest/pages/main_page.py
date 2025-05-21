from selenium.webdriver.common.by import By

from tests.test_selenium.test_pytest.pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
