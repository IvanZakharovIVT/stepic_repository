import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
