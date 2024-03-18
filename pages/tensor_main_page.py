"""Модуль, содержащий методы для работы с https://tensor.ru/."""

from .base_page import BasePage
from .locators import TensorMainPageLocators


class TensorMainPage(BasePage):
    def should_be_tensor_main_page(self):
        """Проверяет, страница ли это https://tensor.ru/."""

        self.should_be_main_page_header()

    def should_be_main_page_header(self):
        """Проверяет наличие соответствующего заголовка."""

        assert self.is_element_present(
            *TensorMainPageLocators.MAIN_PAGE_HEADER
        ), "Tensor Main page header is not presented, therefore it's not Tensor Main page"

    def should_be_power_is_in_people_block(self):
        """Проверяет наличие блока "Сила в людях"."""

        assert self.is_element_present(
            *TensorMainPageLocators.POWER_IS_IN_PEOPLE_BLOCK
        ), "'Power is in people' block is not presented"

    def should_be_power_is_in_people_block_details_link(self):
        """Проверяет наличие ссылки "Подробнее" в блоке "Сила в людях"."""

        assert self.is_element_present(
            *TensorMainPageLocators.POWER_IS_IN_PEOPLE_BLOCK
        ), "'Power is in people' block details is not presented on the Tensor Main Page"

    def go_to_people_is_in_power_details_page(self):
        """Проверяет возможность перехода на другую страницу с использование ссылки "Подробнее"."""

        people_is_in_power_details_page = self.browser.find_element(
            *TensorMainPageLocators.POWER_IS_IN_PEOPLE_DETAILS_LINK
        )
        self.browser.execute_script(
            'return arguments[0].scrollIntoView(true);',
            people_is_in_power_details_page
        )
        people_is_in_power_details_page.click()
