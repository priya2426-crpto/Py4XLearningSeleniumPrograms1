from selenium import webdriver
import allure
import pytest
@allure.title("verify the title of the webpage app.vwo.com")
def test_sample():

    driver=webdriver.Chrome()
    driver.get("http://sdet.live")
    assert driver.current_url=="http://www.sdet.live/"