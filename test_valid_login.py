import pytest


def test_standard_user(page):
    page.visit()

    page.login_as("standard_user", "secret_sauce")

    assert "inventory" in page.get_current_url()
