from selenium import webdriver

def test_open_vwo_login():
    driver=webdriver.Chrome()
    driver.get("http://app.vwo.com")
    # code-->HTTP request -ChromeDriver Selenium Manager -->chrome
    print(driver.title)
    assert driver.title =="Login -VWO"