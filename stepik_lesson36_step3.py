import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def answer_calculate():
    answer = math.log(int(time.time()))
    return str(answer)


@pytest.fixture(scope="function")
def browser():
    print('\nbrowser open')
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    yield browser
    print('\nbrowser quit')
    browser.quit()


@pytest.mark.parametrize('page_id', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
class TestParametrization:
    def test_optional_feedback_vision_correct_response(self, browser, answer_calculate, page_id):
        url = f'https://stepik.org/lesson/{page_id}/step/1'
        browser.get(url)

        answer_box = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text'
                                                                                                        '-area')))
        answer_box.send_keys(answer_calculate)
        answer_send_button = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit'
                                                                                                          '-submission')))
        answer_send_button.click()

        answer_object = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart'
                                                                                                           '-hints__hint')))
        answer = answer_object.text

        assert answer == 'Correct!', f'Not matching the expected and actual text:\n' \
                                     f'AR: {answer}\n' \
                                     f'ER: "Correct!"'
