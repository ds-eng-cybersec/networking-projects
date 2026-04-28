from subnet_calc import calculate_subnet


def test_calculate_subnet():

    result = calculate_subnet("192.168.1.0/24")
    assert result["network_address"] == "192.168.1.0"
    assert result["broadcast_address"] == "192.168.1.255"
    assert result["netmask"] == "255.255.255.0"
    assert result["hostmask"] == "0.0.0.255"
    assert result["number_of_addresses"] == "256"
    assert result["usable_addresses"] == 254
    assert result["host_range"] == "192.168.1.1 - 192.168.1.254"

    result = calculate_subnet("192.168.1.1/32")
    assert result["network_address"] == "192.168.1.1"
    assert result["broadcast_address"] == "192.168.1.1"
    assert result["usable_addresses"] == 0
    assert result["host_range"] == "N/A - Single Host"

    result = calculate_subnet("192.168.1.0/31")
    assert result["usable_addresses"] == 2
    assert result["host_range"] == "192.168.1.0 - 192.168.1.1"

    result = calculate_subnet("10.0.0.0/8")
    assert result["network_address"] == "10.0.0.0"
    assert result["broadcast_address"] == "10.255.255.255"
    assert result["netmask"] == "255.0.0.0"
    assert result["usable_addresses"] == 16777214

    result = calculate_subnet("0.0.0.0/0")
    assert result["network_address"] == "0.0.0.0"
    assert result["broadcast_address"] == "255.255.255.255"
    assert result["usable_addresses"] == 4294967294

    result = calculate_subnet("192.168.1.5/24")
    assert result["network_address"] == "192.168.1.0"
    assert result["broadcast_address"] == "192.168.1.255"

    result = calculate_subnet("::1/128")
    assert result["usable_addresses"] == 0
    assert result["host_range"] == "N/A - Single Host"

    result = calculate_subnet("2001:db8::/127")
    assert result["usable_addresses"] == 2

    result = calculate_subnet("2001:db8::/32")
    assert result["network_address"] == "2001:db8::"
    assert result["usable_addresses"] == 2**96 - 2