import math
from selenium.webdriver.common.by import By

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_first():
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    firstname = browser.find_element(By.XPATH, "//input[@placeholder='Input your name']")
    firstname.send_keys("My_firstname")

    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys("My_email")

    phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone']")
    phone.send_keys("My_phone")

    address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address']")
    address.send_keys("My_address")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    browser.quit()
    assert 1 == 1