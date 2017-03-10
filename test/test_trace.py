from   rstest.general  import get_root_path
from   rstest.savepath import SavePath
from   rstest.settings import default as default_settings
from   rstest.trace    import process_trace
from   rohdeschwarz.instruments.vna import Vna
import os
import unittest


class TestTrace(unittest.TestCase):
	def setUp(self):
		root_path    = get_root_path() / "test_trace"
		serial_no    = "123"
		by_serial_no = True
		self.path    = SavePath(root_path, serial_no, by_serial_no)
		vna = Vna()
		vna.open_tcp()
		vna.clear_status()
		vna.manual_sweep = True
		timeout_ms = 2*vna.sweep_time_ms + 5000
		vna.start_sweeps()
		vna.pause(timeout_ms)
		self.vna = vna
		self.settings = default_settings.copy()

	def tearDown(self):
		self.vna.clear_status()
		self.vna.close()

	@classmethod
	def tearDownClass(self):
		vna = Vna()
		vna.open_tcp()
		vna.close()

	def test_process_trace(self):
		self.path.cd_diagram("diagram_name")
		t_name = self.vna.traces[0]
		data   = process_trace(self.path, self.vna.trace(t_name), self.settings)
		self.assertFalse(self.vna.is_error())

if __name__ == '__main__':
    unittest.main()
