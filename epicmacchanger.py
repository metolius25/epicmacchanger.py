#!/usr/bin/python3
import subprocess
import argparse as agp

parser = agp.ArgumentParser(
                    prog='epicmacchanger.py',
                    description='Simple Python 3 app to specify a new MAC address.\nPro tip: use ip addr to find which interface you want to work on.\nRequires superuser.',
                    epilog='Example usage: python3 mac_changer.py -i eth0 -m 00:00:00:00:00:O0 (Hexadecimal characters only)')
parser.add_argument("-i", "--interface", dest="interface", help="Choose the network interface you want to work on\n", required=True) 
parser.add_argument("-m", "--mac", dest="mac_address", help="Write new MAC Address\n", required=True)

args = parser.parse_args()
interface_var = args.interface
mac_var = args.mac_address

print("\nEpic Mac Changer was just used.\n")

subprocess.call(["sudo", "ip", "link", "set", "dev",interface_var, "down"])
subprocess.call(["sudo", "ip", "link", "set", "dev", interface_var, "address", mac_var])
subprocess.call(["sudo", "ip", "link", "set", "dev", interface_var, "up"])
