from subnet_calc import check_if_valid_entry


def test_check_if_valid_entry() -> None:

    assert check_if_valid_entry("192.168.1.0/24")
    assert check_if_valid_entry("10.0.0.0/8")
    assert check_if_valid_entry("172.16.0.0/16")
    assert check_if_valid_entry("0.0.0.0/0")
    assert check_if_valid_entry("192.168.1.1/32")
    assert check_if_valid_entry("192.168.1.1/24")
    assert check_if_valid_entry("::1/128")
    assert check_if_valid_entry("2001:db8::/32")

    assert not check_if_valid_entry("192.168.1.256/24")
    assert not check_if_valid_entry("192.168.1.0/33")
    assert not check_if_valid_entry("192.168.1.0/-1")
    assert not check_if_valid_entry("not_an_ip")
    assert not check_if_valid_entry("")
    assert not check_if_valid_entry("192.168.1")
    assert not check_if_valid_entry("192.168.1.0/24/32")
    assert not check_if_valid_entry(None)
    assert not check_if_valid_entry(True)
    assert not check_if_valid_entry(False)
    assert not check_if_valid_entry(32)
    assert not check_if_valid_entry(2.0)
