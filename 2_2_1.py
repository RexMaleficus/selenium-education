from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    sum = (int(x) + int(y))
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum))
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(15)
    browser.close()
    browser.quit()
