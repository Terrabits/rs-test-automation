import base64
import os
import json
from   collections  import OrderedDict

from   rstest.channel import process_channel
from   rstest.diagram import process_diagram
from   rstest.general import get_ports
from   rstest.html    import generate as generate_html
from   rstest.vna     import process_vna

def measure(path, vna, test_info = {}):
    # create path
    # if not os.path.exists(str(path)):
    #     os.makedirs(str(path))

    # Sweep, save touchstone
    channels = vna.channels
    for i in channels:
        channel = vna.channel(i)
        ports    = get_ports(vna,channel)
        process_channel(path, channel, ports)

    # VNA screenshot,
    # global pass/fail
    data = process_vna(path, vna)

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
        data['diagrams'][title] = process_diagram(path, vna.diagram(i))

    # summary
    # csv and human readable
    print("data.json")
    with open(str(path / 'data.json'), 'w') as f:
        json.dump(data, f)
    print('test_info.json')
    with open(str(path / 'test_info.json'), 'w') as f:
        json.dump(test_info, f)
    print("summary.html")
    generate_html(str(path / 'summary.html'), test_info, data)
    return data
