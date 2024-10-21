from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure

import pytest
@allure.title("negative Testcase-App.VWO.com")
@allure.description("start a free trial")
def test_negativ_VWO2():
    driver= webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    anchor_tag_element=driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    anchor_tag_element.click()
    assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(5)
    driver.back()