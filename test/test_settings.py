from   rstest.general  import get_root_path
from   rstest.settings import Settings

import unittest

class TestSettings(unittest.TestCase):

	def test_defaults(self):
		s = Settings()
		self.assertEqual(s['dut'], 'DUT')
		self.assertEqual(s['display'], 'default')
		self.assertEqual(s['instrument']['connection type'], 'tcpip')
		self.assertEqual(s['instrument']['address'], '127.0.0.1')
		self.assertEqual(s['save']['directory'], str(get_root_path()))
		self.assertFalse(s['save']['disable global limit'])
		self.assertFalse(s['save']['disable touchstone files'])
		self.assertFalse(s['save']['disable trace csv files'])
		self.assertFalse(s['save']['disable screenshots'])
		self.assertFalse(s['save']['disable per-test limits'])
		self.assertFalse(s['save']['disable markers'])
		self.assertFalse(s['save']['disable html summary'])
		self.assertFalse(s['save']['disable results json'])
		self.assertFalse(s['save']['organize by file'])
		self.assertFalse(s['save']['enable project csv'])
		self.assertTrue(s.is_save_vna())
		self.assertTrue(s.is_save_channels())
		self.assertTrue(s.is_save_diagrams())
		self.assertTrue(s.is_save_traces())

	def test_save_vna(self):
		s = Settings()
		self.assertTrue(s.is_save_vna())
		s['save']['disable global limit'] = True
		self.assertTrue(s.is_save_vna())
		s['save']['disable screenshots']  = True
		self.assertFalse(s.is_save_vna())
		del(s['save']['disable global limit'])
		self.assertTrue(s.is_save_vna())
		del(s['save']['disable screenshots'])

	def test_save_channels(self):
		s = Settings()
		self.assertTrue(s.is_save_channels())
		save = s['save']
		save['disable touchstone files'] = True
		self.assertFalse(s.is_save_channels())
		del(save['disable touchstone files'])
		self.assertTrue(s.is_save_channels())

	def test_save_diagrams(self):
		s = Settings()
		self.assertTrue(s.is_save_diagrams())
		save = s['save']
		keys = ['disable screenshots', 'disable per-test limits']
		for key in keys:
			save[key] = True
		self.assertFalse(s.is_save_diagrams())
		for key in keys:
			del(save[key])
			self.assertTrue(s.is_save_diagrams())
			save[key] = True
			self.assertFalse(s.is_save_diagrams())

	def test_save_traces(self):
		s = Settings()
		self.assertTrue(s.is_save_traces())
		save = s['save']
		keys = ['disable trace csv files', 'disable markers']
		for key in keys:
			save[key] = True
		self.assertFalse(s.is_save_traces())
		for key in keys:
			del(save[key])
			self.assertTrue(s.is_save_traces())
			save[key] = True
			self.assertFalse(s.is_save_traces())

if __name__ == '__main__':
    unittest.main()
