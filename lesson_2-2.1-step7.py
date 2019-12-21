import math
import time

import selenium.webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with selenium.webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/get_attribute.html')
    elem_x = driver.find_element_by_css_selector('#treasure').get_attribute('valuex')
    x = calc(elem_x)
    elem_2 = driver.find_element_by_css_selector('#answer')
    elem_2.send_keys(str(x))
    elem_3 = driver.find_element_by_css_selector('#robotCheckbox')
    elem_3.click()
    elem_4 = driver.find_element_by_css_selector('#robotsRule')
    elem_4.click()
    button = driver.find_element_by_css_selector('button[type="submit"]')
    button.click()
    time.sleep(10)