from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import  time
def test_chrome_options():
        chrome_options=Options()

        driver=webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
        time.sleep(5)
        driver.quit()
def test_edge_options():
        edge_options=Options()

        driver=webdriver.Edge()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
        time.sleep(5)
        driver.quit()


