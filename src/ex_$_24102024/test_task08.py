import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
@allure.title("login")
@allure.description("LOgin hostinger")
def test_07():
    driver = webdriver.Chrome()
    driver.get("/in/login")
    time.sleep(2)

