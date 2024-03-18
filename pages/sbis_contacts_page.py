"""Модуль, содержащий методы для работы с https://sbis.ru/contacts/."""

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import SbisContactsPageLocators


class SbisContactsPage(BasePage):
    def should_be_contacts_page(self):
        """Проверяет """

        self.should_be_contacts_link_selected()
        self.should_be_contacts_header()

    def should_be_contacts_link_selected(self):
        assert self.is_element_present(
            *SbisContactsPageLocators.CONTACTS_LINK_SELECTED
        ), "Contacts link is not selected, therefore it's not Contacts page"

    def should_be_contacts_header(self):
        assert self.is_element_present(
            *SbisContactsPageLocators.CONTACTS_HEADER
        ), "Contacts link is not presented, therefore it's not Contacts page"

    def should_be_tensor_logo_link(self):
        assert self.is_element_present(
            *SbisContactsPageLocators.TENSOR_LOGO_LINK
        ), "Tensor logo link is not presented"

    def go_to_tensor_main_page(self):
        tensor_main_page = self.browser.find_element(
            *SbisContactsPageLocators.TENSOR_LOGO_LINK
        )
        tensor_main_page.click()

    def should_be_region_near_contacts_header(self):
        assert self.is_element_present(
            *SbisContactsPageLocators.GUEST_REGION
        ), "Guest region is not presented"

    def should_be_partners(self):
        assert self.is_element_present(
            *SbisContactsPageLocators.REGION_PARTNERS
        ), "Partners of the specified region aren't presented"

    def go_to_change_region(self):
        region_list = self.browser.find_element(
            *SbisContactsPageLocators.GUEST_REGION
        )
        region_list.click()
        region_selected_by_guest = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((
                SbisContactsPageLocators.REGION_SELECTED_BY_GUEST[0],
                SbisContactsPageLocators.REGION_SELECTED_BY_GUEST[1]
            ))
        )
        region_selected_by_guest.click()

    def should_be_changed_region_in_page_title(self):
        self.go_to_change_region()
        time.sleep(5)
        assert SbisContactsPageLocators.SELECTED_REGION in self.browser.title

    def should_be_changed_region_in_page_url(self):
        self.go_to_change_region()
        time.sleep(10)
        assert SbisContactsPageLocators.SELECTED_REGION_URL in \
            self.browser.current_url

    def should_be_changed_partners(self):
        before_change_partners = self.browser.find_elements(
            *SbisContactsPageLocators.REGION_PARTNERS
        )
        before_change_partners_text = [
            partner.text for partner in before_change_partners
        ]
        self.go_to_change_region()
        time.sleep(5)
        after_change_partners = self.browser.find_elements(
            *SbisContactsPageLocators.REGION_PARTNERS
        )
        after_change_partners_text = [
            partner.text for partner in after_change_partners
        ]
        assert before_change_partners_text != after_change_partners_text
