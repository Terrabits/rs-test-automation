from   rstest.savepath import SavePath
import os
from   pathlib         import Path
import unittest

class TestSavePath(unittest.TestCase):
    def setUp(self):
        return
    def tearDown(self):
        return
    @classmethod
    def tearDownClass(self):
        return

    def test_make_safe_str(self):
        unsafe_str = "/\\:*?\"<>|"
        safe_str = SavePath.make_safe_str(unsafe_str)
        self.assertEqual(safe_str, '~~~~~~~~~')
    def test_expand_user(self):
        path = SavePath('~', 'SerialNo', False)
        self.assertEqual(str(path), os.path.expanduser('~'))
    def test_by_serial_no(self):
        path = SavePath('/save/path', 'SerialNo')
        self.assertEqual(str(path), str(Path('/save/path') / 'SerialNo'))
    def test_cd(self):
        path = SavePath('save/path', 'SerialNo', False)
        path.cd('dir?')
        self.assertEqual(str(path), str(Path('save/path') / 'dir~'))
    def test_cd_up(self):
        path = SavePath('save/path', 'SerialNo', False)
        path.cd_up()
        self.assertEqual(str(path), 'save')
    def test_file_path(self):
        # By file type
        path = SavePath('save/path', 'SerialNo', False)
        file_path = path.file_path(extension=".jpg")
        self.assertEqual(file_path, str(Path('save/path') / "SerialNo.jpg"))
        # By serial no
        path = SavePath('save/path', 'SerialNo')
        file_path = path.file_path(filename="file?name", extension='.ext')
        self.assertEqual(file_path, str(Path('save/path/SerialNo') / 'file~name.ext'))
