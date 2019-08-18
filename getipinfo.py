import ipinfo
import configparser
import argparse

config = configparser.ConfigParser()
config.read("config.ini")

handler = ipinfo.getHandler(config["IPINFO"]["TOKEN"])

parser = argparse.ArgumentParser(
	prog='getipinfo',
	usage='%(prog)s [options]',
	description='%(prog)s - Enter the IP address to get information about!'
)

parser.add_argument(
	'ipaddress',
	type=str,
	help='IP Addres to lookup information about'
)

args = parser.parse_args()

details = handler.getDetails(args.ipaddress)

print(details.all)
