"""Модуль, содержащий тесты для https://sbis.ru/."""

from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contacts_page import SbisContactsPage


def test_guest_can_see_contacts_link(browser):
    """Проверяет наличие ссылки в навигационной панели на https://sbis.ru/contacts/."""

    link = 'https://sbis.ru/'
    page = SbisMainPage(browser, link)
    page.open()
    page.should_be_contacts_link()


def test_guest_can_go_to_contacts_page(browser):
    """Проверяет возможность перехода пользователем на https://sbis.ru/contacts/."""

    link = 'https://sbis.ru/'
    page = SbisMainPage(browser, link)
    page.open()
    page.go_to_contacts_page()
    contacts_page = SbisContactsPage(browser, browser.current_url)
    contacts_page.should_be_contacts_page()
