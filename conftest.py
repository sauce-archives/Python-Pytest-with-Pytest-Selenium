import pytest
from page_sample import SamplePage
from page_sample import InventoryPage


@pytest.fixture
def page(selenium):
    page = SamplePage(selenium)
    return page

@pytest.fixture
def inventory(selenium):
    return InventoryPage(selenium)

