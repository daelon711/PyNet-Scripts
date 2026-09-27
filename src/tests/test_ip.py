

import pytest
from port_scanner import is_ip


def test_valid_ips():
    assert is_ip("192.168.1.1")
    assert is_ip("10.0.0.1")
    assert is_ip("255.255.255.255")


def test_invalid_ips():
    assert not is_ip("256.256.256.256")  # 255<
    assert not is_ip("192.168.1")   # <4
    assert not is_ip("192.168.1.1.1")   # 3<
    assert not is_ip("192.168.1.a")  # non-num
    assert not is_ip(".168.1.1")  # empty
    assert not is_ip("192.168.1.01")  # starts with zero
