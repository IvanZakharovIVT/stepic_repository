import math
from unittest import TestCase
from selenium.webdriver.common.by import By

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

class TestFirst(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.link = "http://suninjuly.github.io/registration2.html"

    def test_first(self):
        self.browser.get(self.link)

        firstname = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        firstname.send_keys("My_firstname")

        lastname = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        lastname.send_keys("My_last_name")

        email = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys("My_email")

        phone = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        phone.send_keys("My_phone")

        address = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        address.send_keys("My_address")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        self.browser.quit()
        self.assertEqual(1, 1)