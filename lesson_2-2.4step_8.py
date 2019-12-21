import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    elem = driver.find_element_by_css_selector('#book')
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    elem.click()
    x = driver.find_element_by_css_selector('#input_value').text
    func = math.log((abs(12*math.sin(int(x)))), math.e)
    ans = driver.find_element_by_css_selector('#answer').send_keys(str(func))
    button = driver.find_element_by_css_selector('#solve').click()
    time.sleep(11)
