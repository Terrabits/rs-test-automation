import os
from   pathlib import Path
import re


class SavePath:
    def __init__(self, root_path, serial_no, by_serial_no=True):
        self.serial_no    = serial_no
        self.by_serial_no = by_serial_no
        self.root_path    = Path(root_path).expanduser()
        self.reset()
    def cd(self, path):
        self.current_dir /= self.make_safe_str(path)
    def cd_up(self):
        self.current_dir = self.current_dir.parent
    def reset(self):
        self.current_dir  = self.root_path
        if self.by_serial_no:
            self.cd(self.serial_no)
    def mkdirs(self):
        self.current_dir.mkdir(parents=True, exist_ok=True)
    def cd_scpi(self):
        self.reset()
        if not self.by_serial_no:
            self.cd('scpi logs')
    def cd_vna_screenshot(self):
        self.reset()
        if not self.by_serial_no:
            self.cd('screenshots')
    def cd_vna_limits(self):
        self.reset()
        if not self.by_serial_no:
            self.cd('limits')
    def cd_channel(self, name):
        self.reset()
        if not self.by_serial_no:
            self.cd('touchstone')
            self.cd(name)
    def cd_diagram(self, title):
        self.diagram = title
        self.reset()
        if not self.by_serial_no:
            self.cd('screenshots')
        self.cd(title)
    def cd_trace(self, name):
        self.reset()
        if not self.by_serial_no:
            self.cd('traces')
        self.cd(self.diagram)
        if not self.by_serial_no:
            self.cd(name)
    def cd_summary(self):
        self.reset()
        if not self.by_serial_no:
            self.cd('summary')
    def cd_json(self):
        self.reset()
        if not self.by_serial_no:
            self.cd('json')
    def file_path(self, filename='', extension=''):
        if self.by_serial_no:
            filename += extension
        else:
            filename = self.serial_no + extension
        return str(self.current_dir / self.make_safe_str(filename))
    def __str__(self):
        return str(self.current_dir)
    def __repr__(self):
        return "SavePath('{0}')".format(self)
    @staticmethod
    def make_safe_str(string):
        return re.sub('[/\\\\:\\*\\?"<>|]', '~', string)
