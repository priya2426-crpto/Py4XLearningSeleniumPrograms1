from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest

@allure.tile("negative Testcase-App.VWO.com")
@allure.description("verify that the mail/password is wrong")
def test_negative_VWO_project2():
    driver=webdriver.Chrome()

    driver.get("http://app.vwo.com")
    anchor_tag_element=driver.find_element(By.LINK_TEXT,"start a free trial")
    anchor_tag_element.click()
    assert driver.current_url=="/wp-content/plugins/vwo-common-templates/intl-tell/js/utils.js?v=2"

    time.sleep(5)
    driver.quit()