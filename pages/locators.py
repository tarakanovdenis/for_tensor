"""Модуль, содержащий локаторы, используемые при работе с веб-страницами."""

from selenium.webdriver.common.by import By


class SbisMainPageLocators:
    """Локаторы для https://sbis.ru/."""

    CONTACTS_LINK = (By.CSS_SELECTOR, 'a[href="/contacts"]')


class SbisContactsPageLocators:
    """Локаторы для https://sbis.ru/contacts/."""

    CONTACTS_LINK_SELECTED = (
        By.CSS_SELECTOR,
        'a.sbisru-Header__menu-link--selected')
    CONTACTS_HEADER = (By.CSS_SELECTOR, 'h2.sbisru-h2.pb-xm-4')
    TENSOR_LOGO_LINK = (
        By.CSS_SELECTOR,
        'img[alt="Разработчик системы СБИС — компания «Тензор»"]'
    )
    GUEST_REGION = (
        By.CSS_SELECTOR,
        '.sbis_ru-Region-Chooser__text.sbis_ru-link'
    )
    REGION_PARTNERS = (
        By.CSS_SELECTOR,
        'div[data-qa="item"]'
    )
    REGION_SELECTED_BY_GUEST = (
        By.CSS_SELECTOR,
        'span[title="Камчатский край"]'
    )
    CONTACTS_PAGE_TITLE = (
        By.CSS_SELECTOR,
        'title.state-1'
    )
    SELECTED_REGION = 'Камчатский край'
    SELECTED_REGION_URL = 'kamchatskij-kraj'


class TensorMainPageLocators:
    """Локаторы для https://tensor.ru/."""

    MAIN_PAGE_HEADER = (
        By.CSS_SELECTOR,
        'h1.tensor_ru-Index__Banner-title'
    )
    POWER_IS_IN_PEOPLE_BLOCK = (
        By.CSS_SELECTOR,
        '.s-Grid-col.s-Grid-col--6'
    )
    POWER_IS_IN_PEOPLE_DETAILS_LINK = (
        By.CSS_SELECTOR,
        'div.s-Grid-col.s-Grid-col--6 a.tensor_ru-link.tensor_ru-Index__link'
    )


class TensorAboutPageLocators:
    """Локаторы для https://tensor.ru/about/."""

    ABOUT_PAGE_HEADER = (
        By.CSS_SELECTOR,
        '.tensor_ru-About__Banner-title'
    )
    WORK_IMAGES = (
        By.CSS_SELECTOR,
        'img.tensor_ru-About__block3-image.new_lazy'
    )
