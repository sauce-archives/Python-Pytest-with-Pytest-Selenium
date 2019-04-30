import pytest
from page_sample import LoginPage
from page_sample import InventoryPage


@pytest.fixture
def login(selenium):
    return LoginPage(selenium)

@pytest.fixture
def inventory(selenium):
    return InventoryPage(selenium)

