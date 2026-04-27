import sys

from subnet_calc import calculate_subnet, check_if_valid_entry

LABELS = {
    "network_address": "Network Address",
    "broadcast_address": "Broadcast Address",
    "netmask": "Subnet Mask",
    "hostmask": "Host Mask",
    "number_of_addresses": "Total Addresses",
    "usable_addresses": "Usable Addresses",
    "host_range": "Host Range",
}

print("> DS-NET-TOOLS // SUBNET-CALC v0.1\n")

while True:
    network_entry = input("Please enter a valid network address (e.g 192.168.1.5/24): ")

    if check_if_valid_entry(network_entry):
        results = calculate_subnet(network_entry)
        for key, value in results.items():
            print(f"{LABELS[key]}: {value}")
        restart_program = input(
            "Would you like to enter another network address? (yes to continue): "
        )
        if restart_program == "yes":
            continue
        else:
            print("\n> Exiting...")
            sys.exit(0)
    else:
        print("The network address you entered is invalid. Please try again.")
