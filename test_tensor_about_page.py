"""Модуль, содержащий тесты для https://tensor.ru/about."""

from .pages.tensor_about_page import TensorAboutPage


def test_guest_can_see_four_images_on_working_block(browser):
    """Проверяет наличие четырех изображений блока "Работаем"."""

    link = 'https://tensor.ru/about'
    tensor_about_page = TensorAboutPage(browser, link)
    tensor_about_page.open()
    tensor_about_page.should_be_tensor_about_page()
    tensor_about_page.should_be_four_images_on_working_block()


def test_whether_four_images_on_working_block_have_similar_height(browser):
    """Проверяет равенство высот четырех изображений блока "Работаем"."""

    link = 'https://tensor.ru/about'
    tensor_about_page = TensorAboutPage(browser, link)
    tensor_about_page.open()
    tensor_about_page.should_be_four_images_with_similar_height()


def test_whether_four_images_on_working_block_have_similar_width(browser):
    """Проверяет равенство ширины четырех изображений блока "Работаем"."""

    link = 'https://tensor.ru/about'
    tensor_about_page = TensorAboutPage(browser, link)
    tensor_about_page.open()
    tensor_about_page.should_be_four_images_with_similar_width()
