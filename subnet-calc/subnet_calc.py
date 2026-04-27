import ipaddress


def check_if_valid_entry(network_entry) -> bool:

    try:
        ipaddress.ip_network(network_entry, strict=False)
        return True
    except ValueError:
        return False


def calculate_subnet(network_entry) -> dict:
    network = ipaddress.ip_network(network_entry, strict=False)
    first_address = network.network_address + 1
    last_address = network.broadcast_address - 1

    max_prefix = 32 if network.version == 4 else 128

    if network.prefixlen == max_prefix:
        usable = 0
        host_range = "N/A - Single Host"
    elif network.prefixlen == max_prefix - 1:
        usable = 2
        host_range = f"{network.network_address} - {network.broadcast_address}"
    else:
        usable = network.num_addresses - 2
        host_range = f"{first_address} - {last_address}"
    return {
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "hostmask": str(network.hostmask),
        "netmask": str(network.netmask),
        "number_of_addresses": str(network.num_addresses),
        "usable_addresses": usable,
        "host_range": host_range,
    }


labels = {
    "network_address": "Network Address",
    "broadcast_address": "Broadcast Address",
    "netmask": "Subnet Mask",
    "hostmask": "Host Mask",
    "number_of_addresses": "Total Addresses",
    "usable_addresses": "Usable Addresses",
    "host_range": "Host Range",
}
