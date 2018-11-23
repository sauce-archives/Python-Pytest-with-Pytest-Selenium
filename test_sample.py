import pytest
from page_sample import SamplePage


@pytest.fixture
def page(selenium):
    page = SamplePage(selenium)
    return page

def test_basic(page):
    page.visit()

    expected = 'Swag Labs'
    actual = page.get_title()

    assert expected == actual

def test_failure(page):
    page.visit()

    expected = 'Incorrect Title'
    actual = page.get_title()

    assert expected == actual

def test_valid_login(page):
    page.visit()

    page.login_as('standard_user', 'secret_sauce')

    expected = 'Swag Labs'
    actual = page.get_header_text()
    
    assert expected == actual

def est_invalid_login(page):
    page.visit()

    page.login_as('bad_user', 'bad_password')

    assert page.is_login_error_visible()

