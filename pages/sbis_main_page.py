"""Модуль, содержащий методы для работы с https://sbis.ru/."""

from .base_page import BasePage
from .locators import SbisMainPageLocators


class SbisMainPage(BasePage):
    def should_be_contacts_link(self):
        """Проверяет наличие ссылки на https://sbis.ru/about/."""

        assert self.is_element_present(
            *SbisMainPageLocators.CONTACTS_LINK
        ), 'Contacts link is not presented.'

    def go_to_contacts_page(self):
        """Проверяет наличие ссылки на https://sbis.ru/about/."""

        contacts_link = self.browser.find_element(
            *SbisMainPageLocators.CONTACTS_LINK
        )
        contacts_link.click()
