"""Модуль, содержащий тесты для https://tensor.ru/."""

from .pages.tensor_main_page import TensorMainPage
from .pages.tensor_about_page import TensorAboutPage


def test_guest_can_see_power_is_in_people_block(browser):
    """Проверяет наличие блока "Сила в людях"."""

    link = 'https://tensor.ru/'
    tensor_main_page = TensorMainPage(browser, link)
    tensor_main_page.open()
    tensor_main_page.should_be_tensor_main_page()
    tensor_main_page.should_be_power_is_in_people_block()


def test_guest_can_see_power_is_in_people_block_details_link(browser):
    """Проверяет наличие ссылки "Подробнее" в блоке "Сила в людях" для перехода на https://tensor.ru/about."""

    link = 'https://tensor.ru/'
    tensor_main_page = TensorMainPage(browser, link)
    tensor_main_page.open()
    tensor_main_page.should_be_tensor_main_page()
    tensor_main_page.should_be_power_is_in_people_block_details_link()


def test_guest_can_go_to_tensor_about_page_using_power_is_in_people_block_details_link(browser):
    """Проверяет возможность перехода на https://tensor.ru/about с помощью ссылки "Подробнее"."""

    link = 'https://tensor.ru/'
    tensor_main_page = TensorMainPage(browser, link)
    tensor_main_page.open()
    tensor_main_page.should_be_tensor_main_page()
    tensor_main_page.should_be_power_is_in_people_block_details_link()
    tensor_main_page.go_to_people_is_in_power_details_page()
    tensor_about_page = TensorAboutPage(browser, browser.current_url)
    tensor_about_page.should_be_tensor_about_page()
