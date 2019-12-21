from selenium import webdriver
import time
import os
BASE_DIR = (os.path.abspath(os.path.dirname(__file__)))
TEXT_F = os.path.join(BASE_DIR, 'hello.txt')
with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/file_input.html')
    elem1 = driver.find_element_by_css_selector('input[name="firstname"]').send_keys("GREWDC")
    elem2 = driver.find_element_by_css_selector('input[name="lastname"]').send_keys("GREWDC")
    elem3 = driver.find_element_by_css_selector('input[name="email"]').send_keys("GREWDC")
    input = driver.find_element_by_css_selector('input[type="file"]').send_keys(TEXT_F)
    but = driver.find_element_by_css_selector('button[type="submit"]')
    but.click()
    time.sleep(10)