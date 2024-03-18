"""Модуль, содержащий тесты для https://sbis.ru/contacts/."""

from .pages.sbis_contacts_page import SbisContactsPage
from .pages.tensor_main_page import TensorMainPage


def test_guest_should_see_tensor_logo_link(browser):
    """Проверяет наличие логотипа-ссылки Тензор."""

    link = 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients'
    contacts_page = SbisContactsPage(browser, link)
    contacts_page.open()
    contacts_page.should_be_contacts_page()
    contacts_page.should_be_tensor_logo_link()


def test_guest_can_go_to_tensor_main_page(browser):
    """Проверяет возможность перехода пользователя на главную страницу Тензор."""

    link = 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients'
    contacts_page = SbisContactsPage(browser, link)
    contacts_page.open()
    contacts_page.should_be_contacts_page()
    contacts_page.go_to_tensor_main_page()
    tensor_main_page = TensorMainPage(browser, browser.current_url)
    browser.switch_to.window(browser.window_handles[1])
    tensor_main_page.should_be_tensor_main_page()


def test_guest_can_see_his_region(browser):
    """Проверяет наличие отображения региона пользователя."""

    link = 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients'
    contacts_page = SbisContactsPage(browser, link)
    contacts_page.open()
    contacts_page.should_be_region_near_contacts_header()


def test_guest_can_go_to_change_his_region(browser):
    """Проверяет возможность изменение региона пользователем."""

    link = 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients'
    contacts_page = SbisContactsPage(browser, link)
    contacts_page.open()
    contacts_page.go_to_change_region()


def test_guest_can_see_changed_region_in_page_title(browser):
    """Проверяет изменение название (title) веб-страницы при изменении региона."""

    link = 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients'
    contacts_page = SbisContactsPage(browser, link)
    contacts_page.open()
    contacts_page.should_be_changed_region_in_page_title()


def test_guest_can_see_changed_region_in_page_url(browser):
    """Проверяет изменение URL веб-страницы при изменении региона."""

    link = 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients'
    contacts_page = SbisContactsPage(browser, link)
    contacts_page.open()
    contacts_page.should_be_changed_region_in_page_url()


def test_guest_can_see_changed_partners(browser):
    """Проверяет изменение списка партнеров при изменении региона."""

    link = 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients'
    contacts_page = SbisContactsPage(browser, link)
    contacts_page.open()
    contacts_page.should_be_changed_partners()
