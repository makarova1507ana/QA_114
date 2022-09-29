import pytest
from pages.yandexSearch.init import YandexSearcher
import time

@pytest.fixture()
def yandex_page():
    return YandexSearcher()

@pytest.fixture()
def browser(yandex_page):
    yandex_page.go_to_site()
    yandex_page.enter_word("cat")
    yield
    yandex_page.quit_from_browser()


def test_search(yandex_page,browser):
    yandex_page.click_on_the_search_button()
    time.sleep(2)


def test_enter_in_field_and_clear_words(yandex_page, browser):
    yandex_page.click_on_cancel_button()
    yandex_page.enter_word("dog")
    yandex_page.click_on_the_search_button()
    time.sleep(2)

def test_check_finding_elements_in_nav_bar(yandex_page, browser):
    yandex_page.click_on_the_search_button()
    elements = yandex_page.find_element_in_nav_bar()
    for i in range(1, len(elements)):
        elements[i].click()
        time.sleep(1)