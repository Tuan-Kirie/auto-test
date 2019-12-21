import math
import time

import selenium.webdriver


with selenium.webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/find_link_text')
    driver.find_element_by_link_text(f"{str(math.ceil(math.pow(math.pi, math.e)*10000))}").click()
    input1 = driver.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id('country')
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector(".btn.btn-default")
    button.click()
    time.sleep(100)