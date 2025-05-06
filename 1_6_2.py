import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=chrome_options)

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
shifr = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    driver.get(link)
    link = driver.find_element(By.LINK_TEXT, shifr)
    link.click()
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)

finally:
    driver.quit()
