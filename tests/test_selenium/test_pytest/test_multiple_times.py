import pytest
import unittest
import math
import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as exc_c
from selenium.webdriver.support.wait import WebDriverWait

from tests.settings import STEPIC_USERNAME, STEPIC_PASSWORD


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

test_list = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

class TestMultipleTime:
    @pytest.mark.parametrize('link', test_list)
    def test_multiple_time(self, browser, link):
        browser.get(link)
        driver_wait = WebDriverWait(browser, 10)

        login_button_prefix = link.split('org')[1]

        driver_wait.until(exc_c.presence_of_element_located(
            (By.XPATH, f"//a[@href='{login_button_prefix}?auth=login']")
        )).click()
        browser.find_element(By.NAME, "login").send_keys(STEPIC_USERNAME)
        browser.find_element(By.NAME, "password").send_keys(STEPIC_PASSWORD)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            driver_wait.until(exc_c.presence_of_element_located(
                (By.XPATH, "//button[@class='again-btn white']")
            )).click()
        except Exception:
            pass
        driver_wait.until(exc_c.element_to_be_clickable(
            (By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']")
        )).send_keys(str(math.log(int(time.time()))))

        driver_wait.until(exc_c.element_to_be_clickable(
            (By.XPATH, "//button[@class='submit-submission']")
        )).click()

        result = WebDriverWait(browser, 10).until(exc_c.presence_of_element_located(
            (By.XPATH, "//p[@class='smart-hints__hint']")
        ))
        print(f"The result is {result.text}")

if __name__ == '__main__':
    unittest.main()
