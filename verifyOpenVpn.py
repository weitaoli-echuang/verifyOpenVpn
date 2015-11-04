from __future__ import print_function
import subprocess
import re
import logging
import os

__author__ = 'VDTConstructor'

logging.basicConfig(level=logging.INFO)


# format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# datefmt='%a, %d %b %Y %H:%M:%S',
# filename='myapp.log',
# filemode='w')
def verify_server(ping_time_out_pattern, server_ip):
	ping_subprocess = subprocess.Popen(['ping', server_ip, '-n', '1'], stdin=None, stdout=subprocess.PIPE, stderr=None)
	ping_output = ''.join(ping_subprocess.stdout.readlines())
	ping_subprocess.kill()

	logging.info(ping_output)
	item_matched = re.findall(ping_time_out_pattern, ping_output)
	if item_matched:
		logging.info('the server could not be reached')
		return None
	else:
		logging.info(str(server_ip) + ' reached')
		return server_ip


def verify_config_file(openvpn_config_file):
	vpn_config = open(openvpn_config_file, 'r').readlines()
	server_pattern = re.compile(r'''(^remote)\s+(\S+)\s+(\d+)''')
	server_ip = list()
	for line in vpn_config:
		server_group = re.match(server_pattern, line)
		if server_group is not None:
			logging.info(server_group.group())
			server_ip.append(server_group.group(2))

	effective_server_list = list()
	for item in server_ip:
		logging.debug('the server ip is')
		logging.debug(item)
		ping_time_out_pattern = re.compile('timed out')
		server = verify_server(ping_time_out_pattern, server_ip)
		if server:
			effective_server_list.append(server)
	return effective_server_list


def verify_configures(dir_path):
	vpn_config_files = list()
	directory = os.path.abspath(dir_path)
	for directory, subdirectories, files in os.walk(directory, topdown=False):
		for f in files:
			vpn_config = os.path.join(directory, f)
			logging.info(vpn_config)

			(path, ext) = os.path.splitext(vpn_config)
			if ext == 'ovpn':
				logging.info('config file find')
				vpn_config_files.append(f)

	verify_config_file('my_expressvpn_usa_-_los_angeles_udp.ovpn')
	logging.info('finished')


def main():
	verify_configures('')
	pass


if __name__ == '__main__':
	main()
