from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure


@allure.title("search macmini in ebay")
@allure.description("")
def test_13():
    driver = webdriver.Chrome()
    driver.get("www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box=driver.find_element(By.XPATH,"//input[@placeholder='search for anything']")
    search_box.send_keys("macmini")
    search_btn=driver.find_element(By.XPATH,"Search")
    search_btn.click()
    time.sleep(5)
    list_of_product_price=driver.find_element(By.CSS_SELECTOR,'.s-item__price')
    list_of_items=driver.find_element(By.CSS_SELECTOR,'.s-item__title')
    assert len(list_of_items) == 62
    print("Total number of items: ", len(list_of_items))
    for i in list_of_items:
        print(i.text)
        time.sleep(5)