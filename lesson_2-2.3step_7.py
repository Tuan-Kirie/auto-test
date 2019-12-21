from selenium import webdriver
import time
import math

with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    trol = driver.find_element_by_css_selector('.trollface.btn.btn-primary').click()
    driver.switch_to.window(driver.window_handles[1])
    elem1 = driver.find_element_by_css_selector('#input_value').text
    func = math.log((abs(12*math.sin(int(elem1)))), math.e)
    answ = driver.find_element_by_css_selector('#answer').send_keys(str(func))
    but = driver.find_element_by_css_selector('button[type="submit"]')
    but.click()
    time.sleep(10)
