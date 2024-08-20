#!/usr/bin/python3
import subprocess
import argparse as agp
import re


def get_Input():
    parser = agp.ArgumentParser(
                    prog='epicmacchanger.py',
                    description='Simple Python app to specify a new MAC address.\nPro tip: use ip addr to find which interface you want to work on.\nRequires superuser.',
                    epilog='Example usage: python3 mac_changer.py -i eth0 -m 00:H1:E2:L3:L4:O5 (Hexadecimal characters only)')
    parser.add_argument("-i", "--interface", dest="interface", help="Choose the network interface you want to work on\n", required=True) 
    parser.add_argument("-m", "--mac", dest="mac_address", help="Write new MAC Address\n", required=True)
    (args) = parser.parse_args()
    return args

def change_Address(interface_var, mac_var):
    subprocess.call(["sudo", "ip", "link", "set", "dev",interface_var, "down"])
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface_var, "address", mac_var])
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface_var, "up"])
    subprocess.call(["sudo", "dhclient", interface_var])


def control_Mac(iface):

    ip_addr = subprocess.check_output(["ip", "addr", "show", iface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ip_addr))
    if new_mac:
        output = new_mac.group(0)
        return output
    else:
        return None

(args) = get_Input()
change_Address(args.interface, args.mac_address)
control_Mac(args.interface)


final_mac = control_Mac(str(args.interface))


if (final_mac == args.mac_address):
    print(f"Program worked successfully. The new MAC Address is {final_mac} ")
else:
    print(f"It appears the mac address you typed ({args.mac_address}) is invalid. Try again")
    

