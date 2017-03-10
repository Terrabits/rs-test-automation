from   rstest.settings import default as default_settings
from   rstest.general  import get_root_path
from   rstest.savepath import SavePath
from   rstest.vna      import process_vna
from   rohdeschwarz.instruments.vna import Vna
import os
import unittest

class TestVna(unittest.TestCase):
	def setUp(self):
		# Path
		root_path    = get_root_path() / "test_vna"
		serial_no    = "123"
		by_serial_no = True
		self.path    = SavePath(root_path, serial_no, by_serial_no)
		# Vna
		vna          = Vna()
		vna.open_tcp()
		vna.clear_status()
		vna.manual_sweep = True
		timeout_ms       = 2*vna.sweep_time_ms + 5000
		vna.start_sweeps()
		vna.pause(timeout_ms)
		self.vna      = vna
		self.settings = default_settings.copy()

	def tearDown(self):
		self.vna.clear_status()
		self.vna.close()

	@classmethod
	def tearDownClass(self):
		vna = Vna()
		vna.open_tcp()
		vna.close()

	def test_process_vna(self):
		data = process_vna(self.path, self.vna, self.settings)
		self.assertFalse(self.vna.is_error())

if __name__ == '__main__':
    unittest.main()
