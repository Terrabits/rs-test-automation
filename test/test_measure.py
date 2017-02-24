import rstest.general
from   rstest.measure                 import measure
from   rohdeschwarz.instruments.vna import Vna
import os
import unittest

class TestMeasure(unittest.TestCase):
	def setUp(self):
		path = rstest.general.get_root_path() / "test_measure"
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

	def test_measure(self):
		measure(self.path, self.vna)

if __name__ == '__main__':
	unittest.main()
