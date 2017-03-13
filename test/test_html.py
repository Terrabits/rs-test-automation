from   rstest.general               import get_root_path
from   rstest.html                  import generate
from   rstest.savepath              import SavePath
from   rstest.settings              import default as default_settings
from   rohdeschwarz.instruments.vna import Vna
import base64
from   collections                  import OrderedDict
import json
import os
from   pathlib                      import Path
import unittest


class TestHtml(unittest.TestCase):
    def setUp(self):
        source_root = os.path.dirname(os.path.realpath(__file__))
        self.source_root = Path(source_root)
        root_path    = get_root_path() / "test_html"
        serial_no    = self.serial_no = "123"
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

    def test_generate(self):
        self.path.mkdirs()
        data_path   = self.source_root / "fixtures" / "data"
        data = None
        data_files = ['full_data']
        for filename in data_files:
            data_file_path = str(data_path / filename)
            data = None
            with open(data_file_path + '.json', 'r') as f:
                data = json.load(f, object_pairs_hook=OrderedDict)
            generate(self.path.file_path(filename + '.html'), self.serial_no, self.settings, data)
        

if __name__ == '__main__':
    unittest.main()
