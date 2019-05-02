import pytest


def test_standard_user(login):
    login.visit()

    login.login_as("standard_user", "secret_sauce")

    assert "inventory" in login.get_current_url()
