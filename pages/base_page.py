"""Модуль, содержащий вспоомгательные методы для работы с драйвером."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Метод для проверки наличия элемента на странице.

            Параметры:
                how : тип локатора
                what : значение локатора (правило поиска элемента CSS)
        """

        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    (how, what)
                )
            )
            self.browser.find_element(
                how,
                what
            )
        except NoSuchElementException:
            return False
        return True
