from   rstest.channel    import process_channel
from   rstest.diagram    import process_diagram, diagram_limits_from_data, strip_limit_from_title
from   rstest.general    import get_ports, timestamp, print_check
from   rstest.html       import generate as generate_html
from   rstest.projectcsv import generate as generate_csv
from   rstest.trace      import process_trace
from   rstest.savepath   import SavePath
from   rstest.vna        import process_vna

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
    data.update(process_vna(path, vna, settings))

    # Diagram screenshots,
    # trace csv,
    # limits
    # markers,
    # other (skew, prop delay)
    if settings.is_save_diagrams() or settings.is_save_traces():
        data['diagrams'] = OrderedDict()
        diagrams = vna.diagrams
        for d in diagrams:
            diagram = vna.diagram(d)
            title   = strip_limit_from_title(diagram.title)
            if title:
                print("Diagram {0}".format(title), flush=True)
            else:
                title = "Diagram {0}".format(diagram.index)
                print(title, flush=True)
            diagram_data = data['diagrams'][title] \
                         = process_diagram(path, diagram, settings)
            traces_data  = diagram_data['traces']  \
                         = OrderedDict()
            if settings.is_save_traces():
                for t in diagram.traces:
                    print("  Trace {0}".format(t), flush=True)
                    trace      = diagram._vna.trace(t)
                    name       = trace.name
                    traces_data[name] = process_trace(path, trace, settings)
            if not settings['save']['disable per-test limits']:
                diagram_limits_from_data(diagram_data)

    # Create summary
    if not settings['save']['disable html summary']:
        print("HTML                ", end='', flush=True)
        path.cd_summary()
        path.mkdirs()
        generate_html(path.file_path('summary', '.html'), serial_no, settings, data)
        print_check()

    # Remove screenshot binary from data
    if not settings['save']['disable screenshots']:
        remove_screenshots(data)

    # Write data
    if not settings['save']['disable results json']:
        print("JSON                ", end='', flush=True)
        path.cd_json()
        path.mkdirs()
        with open(path.file_path('summary', '.json'), 'w') as f:
            json.dump(data, f)
        print_check()
    if settings['save']['enable project csv']:
        print("CSV                 ", end='', flush=True)
        filename = path.root_path / "cumulative.csv"
        filename = str(filename)
        generate_csv(filename, serial_no, data)
        print_check()

    return data
