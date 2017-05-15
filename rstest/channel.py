from   rstest.general import make_path_safe, print_check
import os

def process_channel(path, channel, ports, settings):
    print("Channel {0}".format(channel.name), flush=True)
    if not settings.is_save_channels():
        print("  sweep             ", end='', flush=True)
        channel.sweep()
        print_check()
        return
    ch_name  = channel.name
    path.cd_channel(ch_name)
    path.mkdirs()
    file_ext = ".s{0}p".format(len(ports))
    filename = path.file_path(ch_name, file_ext)
    print("  touchstone        ", end='', flush=True)
    channel.save_measurement_locally(filename, ports)
    print_check()
