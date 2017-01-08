import os
from   pathlib import Path
import re


def get_root_path():
    root_path = os.path.expanduser('~')
    root_path = Path(root_path) / "Documents" / "TestAutomation"
    if not os.path.exists(str(root_path)):
        os.makedirs(str(root_path))
    return root_path

def make_path_safe(s):
    re.sub('[/\\\\:\\*\\?"<>|]', '~', s)
    return s.replace("/", "~")

def get_ports(vna, channel):
    result = []
    for t_name in channel.traces:
        t = vna.trace(t_name)
        ports = t.test_ports()
        for i in ports:
            if not i in result:
                result.append(i)
    return sorted(result)

def touch(filename):
    with open(filename, 'a'):
        os.utime(filename, None)
