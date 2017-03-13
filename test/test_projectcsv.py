from   rstest.general    import get_root_path
from   rstest            import projectcsv
from   rstest.savepath   import SavePath
from   collections       import OrderedDict
import json
import os
from   pathlib           import Path
import unittest

class TestProjectCsv(unittest.TestCase):
    def setUp(self):
        source_root  = os.path.dirname(os.path.realpath(__file__))
        self.source_root = Path(source_root)
        root_path    = get_root_path() / "test_projectcsv"
        self.serial_no    = self.serial_no = "123"
        by_serial_no = False
        self.path    = SavePath(root_path, self.serial_no, by_serial_no)

    def test_generate(self):
        self.path.mkdirs()
        data_path   = self.source_root / "fixtures" / "data"
        data_file   = data_path / 'full_data.json'
        data = None
        with open(str(data_file), 'r') as f:
            data = json.load(f, object_pairs_hook=OrderedDict)
        filename = self.path.root_path / "cumulative.csv"
        filename = str(filename)
        projectcsv.generate(filename, self.serial_no, data)
        
if __name__ == '__main__':
    unittest.main()
