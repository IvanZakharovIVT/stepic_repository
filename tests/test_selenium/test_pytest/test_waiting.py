import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exc_c


import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_waiting():
    try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        result = WebDriverWait(browser, 14).until(
            exc_c.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

        button = browser.find_element(By.ID, "book")
        button.click()

        input_value = browser.find_element(By.ID, 'input_value').text

        browser.find_element(By.ID, 'answer').send_keys(calc(input_value))
        browser.find_element(By.ID, "solve").click()
        time.sleep(1)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
