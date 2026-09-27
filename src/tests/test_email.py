from email_utils import is_valid_email
import pytest


def test_valid_email():
    assert is_valid_email("test@example.com")
    assert is_valid_email("another.test@example.com")


def test_invalid_email():
    assert not is_valid_email("invalidemail")
    assert not is_valid_email("test@example.c")
