import datetime
import os
from   pathlib import Path
import re
import sys
import time


def get_root_path():
    root_path = os.path.expanduser('~')
    root_path = Path(root_path) / "Documents" / "TestAutomation"
    if not os.path.exists(str(root_path)):
        os.makedirs(str(root_path))
    return root_path

def make_path_safe(s):
    return re.sub('[/\\\\:\\*\\?"<>|]', '~', s)

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

def timestamp():
    t_delta  = datetime.timedelta(seconds=time.timezone)
    t_zone   = datetime.timezone(t_delta)
    t_now    = datetime.datetime.now(t_zone).replace(microsecond=0)
    return t_now.isoformat()

def and_keys(keys, mydict):
    result = True
    for key in keys:
        result = result and mydict[key]
    return result
def nand_keys(keys, mydict):
    return not and_keys(keys, mydict)

def print_check():
    sys.stdout.buffer.write(bytes("✓", 'UTF-8'));
    print("", flush=True)
