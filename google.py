from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
browser = webdriver.Chrome(options=chrome_options)

link = "https://www.bing.com/"
search_text = "Ryan Gosling"

try:
    browser.get(link)
    input_field = browser.find_element(By.ID, "sb_form_q")
    input_field.send_keys(search_text)
    input_field.submit()
    browser.find_element(By.XPATH, "(//a[contains(text(),'Изображения')])[1]").click()
    time.sleep(15)

finally:
    browser.close()
    browser.quit()
    
