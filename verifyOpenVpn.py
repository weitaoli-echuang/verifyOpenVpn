from __future__ import print_function

__author__ = 'VDTConstructor'

import subprocess
import re
import logging

logging.basicConfig(level=logging.DEBUG)
                    # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='myapp.log',
                    # filemode='w')


def main():
	vpn_config = open('my_expressvpn_japan_-_tokyo_-_1_udp.ovpn', 'r').readlines()
	# print(vpn_config)
	server_partten = re.compile(r'''(^remote)\s+(\S+)\s+(\d+)''')
	server_ip = list()
	for line in vpn_config:
		server_group = re.match(server_partten, line)
		if server_group is not None:
			print(server_group.group())
			server_ip.append(server_group.group(3))

	for item in server_ip:
		# print(item)
		logging.debug(item)

	ping_subprocess = 

	print('here')
	pass


if __name__ == '__main__':
	main()
