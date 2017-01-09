#!/usr/bin/env python

# rohdeschwarz
from rohdeschwarz.instruments.vna import Vna
from rohdeschwarz.general         import print_header

# rstest
import rstest
from   rstest.general import get_root_path
from   rstest.measure import measure

# stdlib
from   collections    import OrderedDict
import os
from   pathlib        import Path
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

def process_cable(address, serial_number):
	# Connect to VNA
	vna = connect_to_vna(address)
	if not vna:
		return None

	# create dut path
	path     = get_root_path()
	dut_path = path / serial_number
	if not os.path.exists( str(dut_path)):
		os.makedirs( str(dut_path))

	vna.open_log(str(dut_path / "SCPI Log.txt"))
	print_header(vna.log, "R&S USB-C Cable Test Automation", rstest.version)
	vna.print_info()
	vna.is_error()
	vna.clear_status()

	# root path
	root = None
	if getattr(sys, 'frozen', False):
		root = os.path.dirname(sys.executable)
	elif __file__:
		root = os.path.dirname(__file__)

	# test info
	test_info = OrderedDict()
	test_info["dut noun"] = "DUT"
	test_info["serial number"] = serial_number

	# run measurement
	result = measure(dut_path, vna, test_info)

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

	# Connect to VNA
	address = str(raw_input("Enter the IP Address: "))
	print("")
	vna = connect_to_vna(address)
	if not vna:
		sys.exit(0)

	# Create measurement folder
	path    = get_root_path()
	if not os.path.exists( str(path)):
			os.makedirs( str(path))

	# Log vna info
	vna.open_log(str(path / 'SCPI Log.txt'))
	print_header(vna.log, "R&S Test Automation", rstest.version)
	vna.print_info()

	print("Rohde & Schwarz {0} {1}-port\n".format(vna.properties.model, vna.properties.physical_ports))
	print("-------------------\n")

	# Clear previous errors
	vna.is_error()
	vna.clear_status()

	# Close vna connection
	vna.local()
	vna.close()
	vna.close_log()

	# Measure cables until user
	# says stop
	response = None
	while not response in ("n", "no", "q", "quit", "exit"):

		# serial Number
		serial_number = str(raw_input("Please enter the device ID/Serial No: "))
		print("")

		result = process_cable(address, serial_number)
		if not result:
			sys.exit(0)
		elif 'limits' in result:
			message = "Cable {0}"
			message = message.format(result['limits'].upper())
			print(message)
			print("------------\n")
			print("")

		# break?
		print("")
		response = str(raw_input("Measure another cable? (Y/n): "))
		response = response.lower()
		# end while

	# end main
	sys.exit(0)

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc == 2: # check for vna
		address = sys.argv[1]
		vna = connect_to_vna(address)
		if not vna:
			sys.exit(1)
		print_vna_info(vna)
		vna.close()
		sys.exit(0)
	elif argc == 3: # run single measurement
		address       = sys.argv[1]
		serial_number = sys.argv[2]
		result = process_cable(address, serial_number)
		if not result:
			sys.exit(1)
		sys.exit(0)
	else: # Use in console
		main()
