import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stepik.org/catalog?auth=login')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'box')))
    driver.find_element_by_css_selector('input[type="email"]').send_keys('ilgizbariev@mail.ri')
    driver.find_element_by_css_selector('input[type="password"]').send_keys('301190310897Il')
    driver.find_element_by_css_selector('.sign-form__btn.button_with-loader').click()
    time.sleep(3)
    yield driver
    driver.quit()


class TestPage:
    @pytest.mark.parametrize("url", ['https://stepik.org/lesson/236895/step/1',
                                     'https://stepik.org/lesson/236896/step/1',
                                     'https://stepik.org/lesson/236897/step/1',
                                     'https://stepik.org/lesson/236898/step/1',
                                     'https://stepik.org/lesson/236899/step/1',
                                     'https://stepik.org/lesson/236903/step/1',
                                     'https://stepik.org/lesson/236904/step/1',
                                     'https://stepik.org/lesson/236905/step/1'])
    def test_pages(self, url, driver):
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
        text_area = driver.find_element_by_tag_name('textarea')
        answer = math.log(int(time.time()))
        text_area.send_keys(str(answer))
        driver.find_element_by_css_selector('button.submit-submission').click()
        time.sleep(5)
        text = driver.find_element_by_css_selector('.smart-hints__hint').text
        assert text == 'Correct!', f'{text}'
