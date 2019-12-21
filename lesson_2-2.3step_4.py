from selenium import webdriver
import time
import math

with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/alert_accept.html')
    elem = driver.find_element_by_css_selector('button[type="submit"]').click()
    alert = driver.switch_to.alert
    alert.accept()
    elem1 = driver.find_element_by_css_selector('#input_value').text
    func = math.log((abs(12*math.sin(int(elem1)))), math.e)
    inpt = driver.find_element_by_css_selector('#answer').send_keys(str(func))
    but = driver.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(10)