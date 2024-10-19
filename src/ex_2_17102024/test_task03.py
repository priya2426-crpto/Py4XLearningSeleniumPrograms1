from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest
@allure.title('CURA Healthcare Service')
@allure.description("make an appointemnt")

def test_make_appointment():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appintment_element=driver.find_element(By.ID,"btn-make-appointment")
    make_appintment_element.click()
    username=driver.find_element(By.ID, "username")
    username.send_keys("John Deo")
    password=driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")
    login_element=driver.find_element(By.ID,"Login")
    login_element.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(5)
    driver.quit()