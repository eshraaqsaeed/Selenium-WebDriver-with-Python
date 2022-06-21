
import json
import pytest
import selenium.webdriver
from webdriver_manager.chrome import ChromeDriverManager


"""
Race condition happens when actors access the same resource at the same time
    without following an order of operations
-> this can happen whenever autiomation attempts to interact with a page before it is fully
    loaded. Thus, always wait for the target element or page property to be ready.
    
* Two kinds of wait:
    1. Implicit waits are specified once and applied to all interactions
        -> used for small tes automation solutions
    2. Explicit waits must be specified per interaction
        -> more powerful, they can have custom conditions. Better for large test solutions
"""

#driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture
def config(scope="session"):

    # Read file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
        # 1. the browser type is good
        # 2. the implicit wait is an integer value
        # 3. the implicit wait is positive

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # return config so it can be used
    return config

@pytest.fixture
def browser(config):

    # Initialize the ChromeDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opt = selenium.webdriver.ChromeOptions()
        opt.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opt)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 sec for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the Webdriver instance for the setup
    yield b     # generator

    # Quit the Webdriver instance for the clean up
    b.quit()
