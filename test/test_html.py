import rstest.general
from   rstest.html                    import generate
from   rohdeschwarz.instruments.vna import Vna
import base64
from   collections                  import OrderedDict
import json
import os
from   pathlib                      import Path
import unittest


class TestHtml(unittest.TestCase):
    def setUp(self):
        root = os.path.dirname(os.path.realpath(__file__))
        self.root = Path(root)
        path = rstest.general.get_root_path() / "test_html"
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

    def test_generate(self):
        fix_path   = self.root / "fixtures"
        img_path   = fix_path  / "images"
        cable_path = fix_path  / "Cable123"
        test_info = None
        with open(str(cable_path / "test_info.json"), 'r') as f:
            test_info = json.load(f, object_pairs_hook=OrderedDict)
        data = None
        with open(str(cable_path / "data.json"), 'r') as f:
            data = json.load(f, object_pairs_hook=OrderedDict)
        generate(str(self.path / "summary.html"), test_info, data)

if __name__ == '__main__':
    unittest.main()
