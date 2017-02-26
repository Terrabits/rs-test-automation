from   rstest.general import make_path_safe
import os

def process_channel(path, channel, ports, settings):
    ch_name  = channel.name
    path.cd_channel(ch_name)
    if not settings['save']['disable touchstone files']:
        path.mkdirs()
        file_ext = ".s{0}p".format(len(ports))
        filename = path.file_path(ch_name, file_ext)
        print("{0} touchstone file".format(ch_name), flush=True)
        channel.save_measurement_locally(filename, ports)
    else:
        channel.sweep()
