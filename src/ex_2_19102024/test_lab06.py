from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest


def test_chrome_current_url():
    driver=webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    email_webdriver_element=driver.find_element(By.ID,"login-username")
    email_webdriver_element.send_keys("abc@gmail.com")
    password_webdriver_element=driver.find_element(By.Name,"password")
    password_webdriver_element.send_keys("password@1234")
    time.sleep(5)
    driver.quit()