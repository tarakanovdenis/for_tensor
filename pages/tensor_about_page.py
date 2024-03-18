"""Модуль, содержащий методы для работы с https://tensor.ru/about/."""

from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    def should_be_tensor_about_page(self):
        """Проверяет, страница ли это https://tensor.ru/about/"""

        self.should_be_about_page_header()

    def should_be_about_page_header(self):
        """Проверяет наличие соответствующего заголовка."""

        assert self.is_element_present(
            *TensorAboutPageLocators.ABOUT_PAGE_HEADER
        ), "Tensor About page header is not presented, therefore it's not Tensor About page"

    def should_be_four_images_on_working_block(self):
        """Проверяет наличие четырех изображений в блоке "Работаем"."""

        assert 4 == len(self.browser.find_elements(
            *TensorAboutPageLocators.WORK_IMAGES
        )), "The four images on 'Working' block aren't presented"

    def should_be_four_images_with_similar_height(self):
        """Проверяет равенство высот четырех изображений в блоке "Работаем"."""

        image_height_on_working_block = self.browser.find_element(
            *TensorAboutPageLocators.WORK_IMAGES
        ).rect['height']

        working_block_images_on_tensor_about_page = self.browser.find_elements(
            *TensorAboutPageLocators.WORK_IMAGES
        )

        for num, image in enumerate(working_block_images_on_tensor_about_page):
            assert image_height_on_working_block == image.rect['height'], \
                f'{num + 1} image has incorrect value of height.'

    def should_be_four_images_with_similar_width(self):
        """Проверяет равенство ширины четырех изображений в блоке "Работаем"."""

        image_width_on_working_block = self.browser.find_element(
            *TensorAboutPageLocators.WORK_IMAGES
        ).rect['width']

        working_block_images_on_tensor_about_page = self.browser.find_elements(
            *TensorAboutPageLocators.WORK_IMAGES
        )

        for num, image in enumerate(working_block_images_on_tensor_about_page):
            assert image_width_on_working_block == image.rect['width'], \
                f'{num + 1} image has incorrect value of width.'
