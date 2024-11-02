import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
@allure.title("select checkbox")
@allure.description("")
def test_07():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(2)
    gender_element=driver.find_element(By.XPATH,"input[@value='Female']")
    gender_element.click()
    time.sleep(2)
    year_of_experience_element = driver.find_element(By.XPATH, "input[@value='3']")
    year_of_experience_element.click()
    time.sleep(2)
    professional_experience=driver.find_element(By.XPATH, "input[@value='Automation Tester']")
    professional_experience.click()
    time.sleep(2)