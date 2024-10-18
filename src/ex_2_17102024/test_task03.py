from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest
@allure.title('CURA Healthcare Service')
@allure.description("make an appointemnt")
@pytest.mark.smoke
def test_make_appointment(self):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appintment=driver.find_element(By.ID,"btn-make-appointment").click()
    username=driver.find_element(By.ID, "txt-username")
    username.send_keys("John Deo")
    password=driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    login=driver.find_element(By.ID,"btn-login").click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"
    driver.quit()