from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure


@allure.title("finding all the button")
@allure.description("verify that the mail/password is wrong")
def test_4():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    buttons=driver.find_elements(By.TAG_NAME,"Button")
    print(len(buttons))
    for i in buttons:
        print(i.text)

    time.sleep(5)
    driver.quit()