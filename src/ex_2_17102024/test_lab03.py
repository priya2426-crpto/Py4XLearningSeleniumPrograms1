from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_vwo_login():
    driver=webdriver.Chrome()
    driver.get("http://app.vwo.com")
    page_source_date=driver.page_source
    print(page_source_date)