from   rstest.general import make_path_safe
import os

def process_channel(path, channel, ports):
    if not os.path.exists( str(path)):
        os.makedirs( str(path))
    name     = make_path_safe(channel.name)
    filename = str(path / name)
    print("{0}.snp".format(name), flush=True)
    channel.save_measurement_locally(filename, ports)
