
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure


@allure.title("login awesomeqa.com")
@allure.description("Automation for the registrationpage of the AwesomeQA.com/UI")
def test_task05():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name_input_box=driver.find_element(By.ID,"input-firstname")
    first_name_input_box.send_keys("Priya")
    last_name_input_box=driver.find_element(By.ID,"input-lastname")
    last_name_input_box.send_keys("saini")
    email_input_box = driver.find_element(By.XPATH, "//input[@id='input-email']")
    email_input_box .send_keys("sakshi302098@gmail.com")
    telephone_input_box = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    telephone_input_box.send_keys("1234567890")
    password_input_box = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password_input_box .send_keys("project123")
    password_confirm_input_box = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    password_confirm_input_box.send_keys("project123")
    privacy_policy_box=driver.find_element(By.XPATH, "//input[@name='agree']")
    privacy_policy_box.click()
    continue_button=driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    assert driver.current_url=="https://awesomeqa.com/ui/index.php?route=account/success"
    source_page=driver.page_source
    assert "your Account has been created!" in source_page

