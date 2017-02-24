import base64
from   collections  import OrderedDict
import os
import re
from   rstest.general import make_path_safe
from   rstest.trace   import process_trace

def is_skew(title):
    title = title.lower()
    if "skew" in title:
        return True
    else:
        return False
def is_prop_delay(title):
    title = title.lower()
    if "propagation delay" in title:
        return True
    if "prop delay" in title:
        return True
    if "prop. delay" in title:
        return True
    # Else
    return False

def find_50pct(trace):
    trace.delete_markers()
    trace.create_marker(1)
    m_min = trace.marker(1)
    m_min.name = "Min"
    m_min.find_min()

    trace.create_marker(2)
    m_max = trace.marker(2)
    m_max.name = "Max"
    m_max.find_max()

    trace.create_marker(3)
    m_50pct = trace.marker(3)
    m_50pct.name = "50pct"

    m_max_y = m_max.y
    m_min_y = m_min.y
    y_50pct = (m_max_y - m_min_y)/2.0 + m_min_y
    m_50pct.find(y_50pct)
    return m_50pct.x


def delta_50pct(diagram):
    traces = diagram.traces
    if len(traces) != 2:
        return 0
    x = []
    for t in traces:
        t = diagram._vna.trace(t)
        x.append(find_50pct(t))
    return abs(x[0] - x[1])

def process_diagram(path, diagram):
    # Diagram
    title = diagram.title
    if not title:
        title = "Diagram {0}".format(diagram.index)

    # Save screenshot
    path.cd_diagram(title)
    path.mkdirs()
    filename = path.file_path(title, ".png")
    print(title, flush=True)
    diagram.save_screenshot_locally(filename, "PNG")

    # Read screenshot
    data = OrderedDict()
    with open(filename, 'rb') as f:
        data['screenshot'] = base64.b64encode(f.read()).decode()

    # Pass/fail
    data["title"] = title
    if diagram.is_limits():
        if diagram.passed:
            data["limits"] = "passed"
        else:
            data["limits"] = "failed"

    # Diagram macros
    if is_skew(title):
        data["skew"]       = delta_50pct(diagram)
    if is_prop_delay(title):
        data["prop delay"] = delta_50pct(diagram)

    # Process traces
    data['traces'] = OrderedDict()
    for i in diagram.traces:
        trace      = diagram._vna.trace(i)
        name       = trace.name
        data['traces'][name] = process_trace(path, trace)
    return data
