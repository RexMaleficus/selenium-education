from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(15)
    browser.close()
    browser.quit()
