import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Alerts")
@allure.description("verifiy alerts")
def test_alert_jsprompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_Prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_Prompt.click()
    time.sleep(3)
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Priya")
    alert.accept()
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You entered: Priya"
    time.sleep(5)


