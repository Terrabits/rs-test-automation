import rstest.channel
from   rstest.general  import get_root_path
from   rstest.savepath import SavePath
from   rstest.settings import default as default_settings
from   rohdeschwarz.instruments.vna import Vna
import os
import unittest

class TestChannel(unittest.TestCase):
	def setUp(self):
		# Path
		root_path    = get_root_path() / "test_channel"
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
		# Settings
		self.settings = default_settings.copy()

	def tearDown(self):
		self.vna.clear_status()
		self.vna.close()

	@classmethod
	def tearDownClass(self):
		vna = Vna()
		vna.open_tcp()
		vna.close()

	def test_ports_used(self):
		self.assertTrue(True)

	def test_process_channel(self):
		rstest.channel.process_channel(self.path, self.vna.channel(), [1,2], self.settings)
		self.assertFalse(self.vna.is_error())

if __name__ == '__main__':
    unittest.main()
