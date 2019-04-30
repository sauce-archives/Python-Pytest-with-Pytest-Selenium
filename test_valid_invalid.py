import pytest


def test_locked_out_user(page):
    page.visit()

    page.login_as("bad", "bad")

    assert page.is_login_error_visible()
