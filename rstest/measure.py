from   rstest.channel  import process_channel
from   rstest.diagram  import process_diagram, strip_limit_from_title
from   rstest.general  import get_ports,  timestamp
from   rstest.html     import generate as generate_html
from   rstest.trace    import process_trace
from   rstest.savepath import SavePath
from   rstest.vna      import process_vna

from   rohdeschwarz.instruments.vna import Vna

import base64
from   collections     import OrderedDict
import os
import json


def remove_screenshots(data):
    for d in data['diagrams']:
        if 'screenshot' in data['diagrams'][d]:
            del(data['diagrams'][d]['screenshot'])
    return data

def measure(vna, serial_no, settings):
    data = OrderedDict()
    data['timestamp']  = timestamp()

    data['instrument'] = OrderedDict()
    data['instrument']['id string'] = vna.id_string()
    data['instrument']['options']   = vna.options_string()

    path = SavePath(settings['save']['directory'], serial_no, not settings['save']['organize by file'])
    path.mkdirs()

    # Sweep, save touchstone
    channels = vna.channels
    for i in channels:
        channel = vna.channel(i)
        ports   = get_ports(vna, channel)
        process_channel(path, channel, ports, settings)

    # VNA screenshot,
    # global pass/fail
    result = process_vna(path, vna, settings);
    data.update(result)

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
        if not title:
            title = "Diagram {0}".format(diagram.index)
        title   = strip_limit_from_title(title)
        diagram_data = data['diagrams'][title] \
                     = process_diagram(path, diagram, settings)
        traces_data  = diagram_data['traces']  \
                     = OrderedDict()
        for i in diagram.traces:
            trace      = diagram._vna.trace(i)
            name       = trace.name
            traces_data[name] = process_trace(path, trace, settings)

    # Create summary
    if not settings['save']['disable html summary']:
        path.cd_summary()
        path.mkdirs()
        print("summary.html", flush=True)
        generate_html(path.file_path('summary', '.html'), serial_no, settings, data)

    # Remove screenshot binary from data
    remove_screenshots(data)

    # Write data
    if not settings['save']['disable results json']:
        print("data.json", flush=True)
        path.cd_json()
        path.mkdirs()
        with open(path.file_path('summary', '.json'), 'w') as f:
            json.dump(data, f)

    return data
