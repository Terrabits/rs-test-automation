import base64
import os
import json
from   collections     import OrderedDict

from   rstest.channel  import process_channel
from   rstest.diagram  import process_diagram
from   rstest.general  import get_ports,  timestamp
from   rstest.html     import generate as generate_html
from   rstest.savepath import SavePath
from   rstest.vna      import process_vna

from   rohdeschwarz.instruments.vna import Vna

def remove_screenshots(data):
    for d in data['diagrams']:
        del(data['diagrams'][d]['screenshot'])
    return data

def measure(vna, serial_no, settings):
    data = OrderedDict()
    data['timestamp']  = timestamp()

    data['instrument'] = OrderedDict()
    data['instrument']['id string'] = vna.id_string()
    data['instrument']['options']   = vna.options_string()

    save_path = SavePath(settings['save']['directory'], serial_no, not settings['save']['organize by file'])
    save_path.mkdirs()

    # Sweep, save touchstone
    channels = vna.channels
    for i in channels:
        channel = vna.channel(i)
        ports   = get_ports(vna,channel)
        process_channel(save_path, channel, ports)

    # VNA screenshot,
    # global pass/fail
    data.update(process_vna(save_path, vna))

    # Diagram screenshots,
    # trace csv,
    # limits
    # markers,
    # other (skew, prop delay)
    data['diagrams'] = OrderedDict()
    diagrams = vna.diagrams
    for i in diagrams:
        diagram = vna.diagram(i)
        title   = diagram.title
        data['diagrams'][title] = process_diagram(save_path, vna.diagram(i))

    # Create summary
    if not settings['save']['disable html summary']:
        save_path.cd_summary()
        save_path.mkdirs()
        print("summary.html", flush=True)
        generate_html(save_path.file_path('summary', '.html'), serial_no, settings['dut'], data)

    # Remove screenshot binary from data
    remove_screenshots(data)

    # Write data
    if not settings['save']['disable results json']:
        print("data.json", flush=True)
        save_path.cd_json()
        save_path.mkdirs()
        with open(save_path.file_path('summary', '.json'), 'w') as f:
            json.dump(data, f)

    return data
