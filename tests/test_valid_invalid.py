import pytest


def test_locked_out_user(login):
    login.visit()

    login.login_as("bad", "bad")

    assert login.is_login_error_visible()
