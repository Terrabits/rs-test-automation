import rstest.diagram
import rstest.general
from   rohdeschwarz.instruments.vna import Vna
from   ddt      import ddt, data
import os
import unittest


@ddt
class TestDiagram(unittest.TestCase):
	def setUp(self):
		path = rstest.general.get_root_path() / "test_diagram"
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

	# def test_ports_used(self):
	# 	self.assertTrue(True)

	@data({'title': '',                'is_skew': False},
		  {'title': 'My measurement',  'is_skew': False},
		  {'title': 'Intra-pair skew', 'is_skew': True },
		  {'title': 'IntraPairSkew',   'is_skew': True })
	def test_is_skew(self, data):
		self.assertEqual(rstest.diagram.is_skew(data['title']), data['is_skew'])

	@data({'title': '',                  'is_prop_delay': False},
		  {'title': 'My measurement',    'is_prop_delay': False},
		  {'title': 'Prop delay',        'is_prop_delay': True },
		  {'title': 'My prop. delay',    'is_prop_delay': True },
		  {'title': 'Propagation delay', 'is_prop_delay': True })
	def test_is_prop_delay(self, data):
		self.assertEqual(rstest.diagram.is_prop_delay(data['title']), data['is_prop_delay'])

	def test_process_diagram(self):
		data = rstest.diagram.process_diagram(self.path, self.vna.diagram())
		data['screenshot'] = bool(data['screenshot'])
		print(data)
		self.assertFalse(self.vna.is_error())

if __name__ == '__main__':
	unittest.main()
