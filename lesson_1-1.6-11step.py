from selenium import webdriver
import time
link_1 = 'http://suninjuly.github.io/registration1.html'
link_2 = 'http://suninjuly.github.io/registration2.html'
with webdriver.Chrome() as driver:
    driver.get(link_1)
    elem_1 = driver.find_element_by_css_selector('.form-control.first')
    elem_2 = driver.find_element_by_css_selector('.form-control.second[placeholder="Input your last name"]')
    elem_3 = driver.find_element_by_css_selector('.form-control.third')
    button = driver.find_element_by_css_selector('button[type="submit"]')
    elem_1.send_keys("DIZZZYDUSTIN")
    elem_2.send_keys("DIZZZYDUSTIN")
    elem_3.send_keys("DIZZZYDUSTIN")
    button.click()
    time.sleep(10)
    driver.get(link_2)
    elem_1 = driver.find_element_by_css_selector('.form-control.first')
    elem_2 = driver.find_element_by_css_selector('.form-control.second[placeholder="Input your last name"]')
    elem_3 = driver.find_element_by_css_selector('.form-control.third')
    button = driver.find_element_by_css_selector('button[type="submit"]')
    elem_1.send_keys("DIZZZYDUSTIN")
    elem_2.send_keys("DIZZZYDUSTIN")
    elem_3.send_keys("DIZZZYDUSTIN")
    time.sleep(10)
