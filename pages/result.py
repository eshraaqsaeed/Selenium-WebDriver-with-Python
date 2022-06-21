"""
This module contains DuckDuckGo page
the page object for the DuckDuckGo page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    # interaction methods

    def result_link_titles(self):
        # TODO
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self, phrase):
        # TODO
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        # TODO
        return self.browser.title
