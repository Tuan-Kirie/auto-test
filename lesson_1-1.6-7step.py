from selenium import webdriver
import time


with webdriver.Chrome() as driver:
    driver.get("http://suninjuly.github.io/find_xpath_form")
    elements = driver.find_elements_by_tag_name("input")
    for k in elements:
        k.send_keys("Мой ответ")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(20)