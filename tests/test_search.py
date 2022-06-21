import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

"""
Every test case should have its own webdriver instance
Each test should initialize a fresh webdriver instance as part of setup
    and then it should quit the instance as part of clean-up
   -> test case should be independent from each other that means no test case should
        share any resources or dependencies with another otherwise problems in one test case could impact others 
            -> thus, can't be parallelized

"""

################

"""
* Elements needed for our test here are:
    1. the search input on the DDG search page
    2. the search input on the DDG result page
    3. the result links on the DDG result page
"""

@pytest.mark.parametrize('phrase', ['turkey', 'aurora'])
def test_basic_duckduckgo_search(browser, phrase):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user search for "Aurora"
    search_page.search(phrase)

    # Then the search result query is "Aurora"
    assert phrase == result_page.search_input_value(phrase)

    # And the search result query is "Aurora"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # TODO: Remove this exception once the test is complete
    #raise Exception("Incomplete Test")

    # And the search result title contains "aurora"
    assert phrase in result_page.title()

