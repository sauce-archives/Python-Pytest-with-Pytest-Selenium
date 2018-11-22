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
