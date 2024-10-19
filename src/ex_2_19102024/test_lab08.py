from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest

@allure.tile("negative Testcase-App.VWO.com")
@allure.description("verify that theemail/password is wrong")
def test_negative_VWO_project2():
    driver=webdriver.Chrome()

    driver.get("http://app.vwo.com")
    email_webdriver_element=driver.find_element(By.ID,"login-username")
    email_webdriver_element.send_keys("abc@gmail.com")
    password_webdriver_element=driver.find_element(By.,"password")
    password_webdriver_element.send_keys("password@1234")
    submit_btn_element=driver.find_element(By.ID, "js-require")
    submit_btn_element.click()
    #error_message_web_element=driver.find_element((By.CLASS_NAME, "notification-box-description")
    #assert error_message_web_element.text=="Your email,password,IP address or location did not match"
    time.sleep(5)
    driver.quit()