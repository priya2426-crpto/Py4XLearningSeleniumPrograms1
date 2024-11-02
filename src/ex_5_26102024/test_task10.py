import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
@allure.title("Action p3")
@allure.description("verify click del")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    #fromcity = driver.find_element(By.XPATH,"//div[text().'From']")
WebDriverWait(driver=driver,timeout=5).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep']")))
    fromcity = driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1kihuf0 r-13awgt0 r-1tsuqlv r-a2ipxf r-1jwulwa r-13qz1uu]")
    time.sleep(5)
    actions = ActionChains(driver)
    (actions.
     move_to_element(fromcity)
     .click().send_keys("del")  # for delhi type del
     .perform())
    time.sleep(5)

    driver.quit()










