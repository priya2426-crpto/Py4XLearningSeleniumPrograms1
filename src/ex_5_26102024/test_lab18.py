import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
@allure.title("Action p1")
@allure.description("verify action p1")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    First_name= driver.find_element(By.XPATH,"//input[@name='firstname']")
    actions=ActionChains(driver= driver)
    (actions
     .key_down(Keys.SHIFT)
     .send_keys_to_element(First_name,"the testing academy")
     .key_up(Keys.SHIFT).perform()
     )
    time.sleep(10)


