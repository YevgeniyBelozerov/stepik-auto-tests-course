from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

browser = webdriver.Firefox()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))

    browser.find_element_by_id('book').click()
    inputValue = browser.find_element_by_id('input_value')
    x = inputValue.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    answerForm = browser.find_element_by_id('answer')
    submit = browser.find_element_by_id('solve')
    answerForm.send_keys(y)
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
