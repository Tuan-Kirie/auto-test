from selenium import webdriver
import time
with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/selects1.html')
    el1 = driver.find_element_by_css_selector('#num1')
    el2 = driver.find_element_by_css_selector('#num2')
    sum = int(el1.text) + int(el2.text)
    sel_1 = driver.find_element_by_css_selector('#dropdown').click()
    sel_2 = driver.find_elements_by_css_selector('#dropdown > option')
    for el in range(len(sel_2)):
        if sel_2[el].text == str(sum):
            sel_2[el].click()
            break
    but = driver.find_element_by_css_selector('button[type="submit"]').click()

    time.sleep(10)