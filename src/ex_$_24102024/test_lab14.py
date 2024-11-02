from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure


@allure.title("click on button")
@allure.description("click on button an submit theawesomeqa")
def test_task14():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    gener_name_selection = driver.find_element(By.CSS_SELECTOR, "")