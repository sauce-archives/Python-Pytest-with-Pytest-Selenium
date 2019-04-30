import pytest
from page_sample import SamplePage


@pytest.fixture
def page(selenium):
    page = SamplePage(selenium)
    return page

