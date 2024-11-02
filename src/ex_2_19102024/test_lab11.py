from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure


@allure.title("find all the buttons by tagName")
@allure.description("verified that the free trail button is clicked, navigated to next page")
def test_05():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name_input_box=driver.find_element(By.XPATH,"//input[@name='firstname']")
    first_name_input_box.send_keys("Hello")
    time.sleep(5)