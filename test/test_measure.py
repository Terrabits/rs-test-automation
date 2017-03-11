from   rstest.general               import get_root_path
from   rstest.measure               import measure
from   rstest.settings import default as   default_settings
from   rohdeschwarz.instruments.vna import Vna
import os
import unittest

class TestMeasure(unittest.TestCase):
	def setUp(self):
		self.serial_no = "123"
		self.settings  = default_settings.copy()
		path = get_root_path() / "test_measure"
		self.settings['save']['directory'] = path
		vna  = Vna()
		vna.open_tcp()
		vna.clear_status()
		self.vna = vna

	def tearDown(self):
		self.vna.clear_status()
		self.vna.close()

	@classmethod
	def tearDownClass(self):
		vna = Vna()
		vna.open_tcp()
		vna.close()

	def test_measure_all(self):
		measure(self.vna, self.serial_no, self.settings)

	def test_measure_nothing(self):
		# Disable everything
		settings = default_settings.copy()
		save = settings['save']
		dir = save['directory']
		display = save['display']
		for key in save:
			save[key] = True;
		save['directory'] = dir
		save['display'] = display
		measure(self.vna, self.serial_no, settings)

if __name__ == '__main__':
	unittest.main()
