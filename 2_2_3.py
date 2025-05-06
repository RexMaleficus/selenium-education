from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"
text = "TestText"
file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '223file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for element in elements:
        element.send_keys(text)
    browser.find_element(By.ID, "file").send_keys(file)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(15)
    browser.close()
    browser.quit()
