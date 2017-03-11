#!/usr/bin/env python

# rohdeschwarz
from rohdeschwarz.instruments.vna import Vna
from rohdeschwarz.general         import print_header

# rstest
import rstest
from   rstest.general  import get_root_path
from   rstest.measure  import measure
from   rstest.savepath import SavePath
from   rstest.settings import Settings
from   rstest.settings import default as default_settings

# python
import json
import sys

def connect_to_vna(address):
	vna = Vna()
	try:
		vna.open_tcp(address)
	except:
		print("\n\n* Error!\n*  Problem connecting to VNA at ip {0}".format(address))
		return None
	try:
		if not vna.connected():
			print("\n\n* Error!\n*  Problem connecting to VNA at ip {0}".format(address))
			return None
		if not vna.properties.is_known_model():
			print("\n\n* Error!\n*  Could not find R&S VNA at ip {0}".format(address))
			print("*   *IDN? response: {0}".format(vna.id_string()))
			return None;
	except:
		print("\n\n* Error!\n*  Problem connecting to VNA at ip {0}".format(address))
		return None
	# set long timeout,
	vna.timeout_ms = 60000
	return vna

def print_vna_info(vna):
	log = vna.log
	vna.log = sys.stdout
	vna.print_info()
	vna.log = log

def process_dut(serial_no, settings):
	# Connect to VNA
	vna = connect_to_vna(settings['instrument']["address"])
	if not vna:
		return None

	# Save path
	save_path = SavePath(settings["save"]["directory"], serial_no, not settings['save']['organize by file'])
	save_path.mkdirs()

	# Create scpi log
	save_path.cd_scpi()
	save_path.mkdirs()
	vna.open_log(save_path.file_path("SCPI Log", ".txt"))
	print_header(vna.log, "R&S Test Automation", rstest.version)
	vna.print_info()
	vna.is_error()
	vna.clear_status()

	# run measurement
	result = measure(vna, serial_no, settings)

	# check for errors,
	# close log
	vna.is_error()
	vna.clear_status()
	vna.close_log()
	return result

def main():
	print("")
	print("R&S Test Automation")
	print("===================\n")

	# For now...
	settings = default_settings.copy()

	# Connect to VNA
	settings["instrument"]["address"] = str(input("Enter the IP Address: "))
	print()
	vna = connect_to_vna(settings['instrument']['address'])
	if not vna:
		sys.exit(0)

	# Save path
	save_path = SavePath(settings["save"]["directory"], '')
	save_path.mkdirs()

	# Create scpi log
	vna.open_log(save_path.file_path("SCPI Log.txt"))
	print_header(vna.log, "R&S Test Automation", rstest.version)
	vna.print_info()
	vna.is_error()
	vna.clear_status()

	print("Rohde & Schwarz {0} {1}-port\n".format(vna.properties.model, vna.properties.physical_ports))
	print("-------------------\n")

	# Close vna connection
	vna.local()
	vna.close()
	vna.close_log()

	# Measure DUTs until user
	# says stop
	response = None
	while not response in ("n", "no", "q", "quit", "exit"):

		# serial Number
		serial_number = str(input("Please enter the device ID/Serial No: "))
		print()

		result = process_dut(serial_number, settings)
		if not result:
			sys.exit(0)
		elif 'limits' in result:
			message = "DUT {0}"
			message = message.format(result['limits'].upper())
			print(message)
			print("------------\n")
			print()

		# break?
		print()
		response = str(input("Measure another DUT? (Y/n): "))
		response = response.lower()
		# end while

	# end main
	sys.exit(0)

if __name__ == "__main__":
	argc = len(sys.argv)
	# VNA connection check
	# run <ip_address>
	if argc == 2:
		address = sys.argv[1]
		vna = connect_to_vna(address)
		if not vna:
			sys.exit(1)
		print_vna_info(vna)
		vna.close()
		sys.exit(0)
	# Single measurement
	# run <serial_no> <settings_json_str>
	elif argc == 3:
		print(sys.argv[0], flush=True);
		print(sys.argv[1], flush=True);
		print(sys.argv[2], flush=True);
		serial_number = sys.argv[1]
		settings = Settings(json.loads(sys.argv[2]))
		result = process_dut(serial_number, settings)
		if not result:
			sys.exit(1)
		sys.exit(0)
	# Command-line interface
	else:
		main()
