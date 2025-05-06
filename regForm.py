from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
browser = webdriver.Chrome(options=chrome_options)

link = "http://suninjuly.github.io/registration1.html"
text = "Test"


try:
    browser.get(link)
    fields = browser.find_elements(By.CSS_SELECTOR, "input[required]")
    for field in fields:
        field.send_keys(text)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(15)
    browser.close()
    browser.quit()