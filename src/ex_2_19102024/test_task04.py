from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure


@allure.title("app.vwo login")
@allure.description("verify that the mail/password is wrong")
def test_task04():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_webdriver_element=driver.find_element(By.ID,"login-username")
    email_webdriver_element.send_keys("abc@gmail.com")
    password_webdriver_element=driver.find_element(By.ID,"login-password")
    password_webdriver_element.send_keys("password@123")
    submit_btn_element=driver.find_element(By.XPATH, "js-captcha-wrap")
    submit_btn_element.click()
    time.sleep(3)
    error_message=driver.find_element(By.CLASS_NAME,"js-notification-box-msg")
    print(error_message.text)
    error_message = driver.page_source
    assert error_message=='your email,password,IP address,IP address or location did not amtch' in error_message
    time.sleep(5)
