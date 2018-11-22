import pytest


@pytest.fixture
def capabilities(capabilities):
    capabilities['browserName'] = 'Firefox'
    capabilities['version'] = '59.0'
    capabilities['platform'] = 'Windows 10'

    return capabilities

def test_basic(selenium):
    selenium.get('https://www.saucedemo.com')

    expected = 'Swag Labs'
    actual = selenium.title

    assert expected == actual

def test_valid_login(selenium):
    selenium.get('https://www.saucedemo.com')

    selenium.find_element_by_css_selector('[data-test="username"]').send_keys('standard_user')
    selenium.find_element_by_css_selector('[data-test="password"]').send_keys('secret_sauce')
    selenium.find_element_by_css_selector('.login-button').click()

    expected = 'Swag Labs'
    actual = selenium.find_element_by_id('header_container').text
    
    assert expected == actual

def test_invalid_login(selenium):
    selenium.get('https://www.saucedemo.com')

    selenium.find_element_by_css_selector('[data-test="username"]').send_keys('bad_user')
    selenium.find_element_by_css_selector('[data-test="password"]').send_keys('bad_pass')
    selenium.find_element_by_css_selector('.login-button').click()

    assert selenium.find_element_by_css_selector('.error-button').is_displayed()

