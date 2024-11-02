import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
@allure.title("Action P4")
@allure.description("drag an drop")
def test_verify_action_mouse():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    time.sleep(2)
    input_element=driver.find_element(By.ID,"clickable")
    input_element.send_keys("priya")
    source_element = driver.find_element(By.ID, 'draggable')
    target_element = driver.find_element(By.ID, 'droppable')

    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()

    time.sleep(2)

    driver.quit()


