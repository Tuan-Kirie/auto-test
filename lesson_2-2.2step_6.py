from selenium import webdriver
import time
import math



with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/execute_script.html')
    x = driver.find_element_by_css_selector('#input_value.nowrap').text
    answer = math.log((abs(12*math.sin(int(x)))), math.e)
    print(answer)
    answer_elem = driver.find_element_by_css_selector('#answer')
    answer_elem.send_keys(str(answer))
    check_box = driver.find_element_by_css_selector('input[type="checkbox"]')
    check_box.click()
    driver.execute_script("""button = document.getElementsByTagName("button")[0];
    button.scrollIntoView();""")
    radio_box = driver.find_element_by_css_selector('input[value="robots"]')
    radio_box.click()
    button = driver.find_element_by_tag_name("button").click()
    time.sleep(10)