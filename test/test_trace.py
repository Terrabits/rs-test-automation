import rstest.general
import rstest.trace
from   rohdeschwarz.instruments.vna import Vna
import os
import unittest


class TestTrace(unittest.TestCase):
	def setUp(self):
		path = rstest.general.get_root_path() / "test_trace"
		if not os.path.exists(str(path)):
			os.makedirs(str(path))
		self.path = path
		vna = Vna()
		vna.open_tcp()
		vna.clear_status()
		vna.manual_sweep = True
		timeout_ms = 2*vna.sweep_time_ms + 5000
		vna.start_sweeps()
		vna.pause(timeout_ms)
		self.vna = vna

	def tearDown(self):
		self.vna.clear_status()
		self.vna.close()

	@classmethod
	def tearDownClass(self):
		vna = Vna()
		vna.open_tcp()
		vna.close()

	def test_process_trace(self):
		t_name = self.vna.traces[0]
		data   = rstest.trace.process_trace(self.path, self.vna.trace(t_name))
		self.assertFalse(self.vna.is_error())

if __name__ == '__main__':
    unittest.main()
