import unittest
import time
from selenium import webdriver


class TestRegistration(unittest.TestCase):
    def test_registration_page_1(self):
        with webdriver.Chrome() as driver:
            driver.get('http://suninjuly.github.io/registration1.html')
            elem_1 = driver.find_element_by_css_selector('.form-control.first')
            elem_2 = driver.find_element_by_css_selector('.form-control.second[placeholder="Input your last name"]')
            elem_3 = driver.find_element_by_css_selector('.form-control.third')
            button = driver.find_element_by_css_selector('button[type="submit"]')
            elem_1.send_keys("DIZZZYDUSTIN")
            elem_2.send_keys("DIZZZYDUSTIN")
            elem_3.send_keys("DIZZZYDUSTIN")
            button.click()
            check = driver.find_element_by_css_selector('h1').text
            assert check == 'Congratulations! You have successfully registered!'

    def test_registration_page_2(self):
        with webdriver.Chrome() as driver:
            driver.get('http://suninjuly.github.io/registration2.html')
            elem_1 = driver.find_element_by_css_selector('.form-control.first')
            elem_2 = driver.find_element_by_css_selector('.form-control.second[placeholder="Input your last name"]')
            elem_3 = driver.find_element_by_css_selector('.form-control.third')
            button = driver.find_element_by_css_selector('button[type="submit"]')
            elem_1.send_keys("DIZZZYDUSTIN")
            elem_2.send_keys("DIZZZYDUSTIN")
            elem_3.send_keys("DIZZZYDUSTIN")
            button.click()
            check = driver.find_element_by_css_selector('h1').text
            assert check == 'Congratulations! You have successfully registered!'


if __name__ == "__main__":
    unittest.main()
