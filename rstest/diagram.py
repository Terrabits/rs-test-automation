from   rstest.general import make_path_safe
from   rstest.trace   import process_trace

from   rohdeschwarz.general  import to_float

import base64
from   collections    import OrderedDict
import os
import re


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

def limit_in_title(title):
    limits_str_re = re.compile('(?:\\[)((?:(?:[^,]+),?)+)(?:\\])$')
    limits_strs = limits_str_re.findall(title)
    if limits_strs:
        return limits_strs[0]
    else:
        return None

def strip_limit_from_title(title):
    limit_str = limit_in_title(title);
    if not limit_str:
        return title
    return title[:-(len(limit_str)+2)].strip()

def eval_limit(limit_str, value):
    compare_op, num_str = limit_str.split(":")
    compare_op = compare_op.strip().lower()
    limit      = to_float(num_str)
    if compare_op == "max":
        return value <= limit
    if compare_op == "min":
        return value >= limit
    # Did not recognize operator
    return False

def eval_limits(title, value):
    limits_str    = limit_in_title(title)
    limit_strs    = limits_str.split(',')
    is_pass = True
    for limit_str in limit_strs:
        is_pass = is_pass and eval_limit(limit_str, value)
    return is_pass

def process_skew(diagram, title):
    data = OrderedDict()
    if is_skew(title):
        print('Calculating skew', flush=True)
        value        = delta_50pct(diagram)
        data["skew"] = value
        if limit_in_title(title):
            is_passed = eval_limits(title, value)
            if not is_passed:
                data['limits'] = "failed"
            elif 'limits' not in data:
                data['limits'] = "passed"
    return data

def process_prop_delay(diagram, title):
    data = OrderedDict()
    if is_prop_delay(title):
        print('Calculating prop delay', flush=True)
        value              = delta_50pct(diagram)
        data["prop delay"] = value
        if limit_in_title(title):
            is_passed = eval_limits(title, value)
            if not is_passed:
                data['limits'] = "failed"
            elif 'limits' not in data:
                data['limits'] = "passed"
    return data

def save_diagram_screenshot(path, diagram, title):
    path.mkdirs()
    filename = path.file_path(title, ".png")
    print(title, flush=True)
    diagram.save_screenshot_locally(filename, "PNG")
    with open(filename, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def diagram_limits_from_data(diagram_data):
    print("Evaluating {} limits".format(diagram_data['title']), flush=True)
    for t_name in diagram_data['traces']:
        trace_data = diagram_data['traces'][t_name]
        if 'limits' in trace_data:
            if trace_data['limits'] == 'failed':
                diagram_data['limits'] = 'failed'
            elif trace_data['limits'] and not diagram_data['limits']:
                diagram_data['limits'] = trace_data['limits']
    return diagram_data

def process_diagram(path, diagram, settings):
    # title, path
    data = OrderedDict()
    title = diagram.title
    if not title:
        title = "Diagram {0}".format(diagram.index)
    path.cd_diagram(strip_limit_from_title(title))
    data["title"] = strip_limit_from_title(title)
    print(data['title'], flush=True)

    # Diagram macros
    if not settings['save']['disable markers']:
        data.update(process_skew(diagram, title))
        data.update(process_prop_delay(diagram, title))

    # Screenshot
    if not settings['save']['disable screenshots']:
        data['screenshot'] = save_diagram_screenshot(path, diagram, title)

    # Limits
    # ... do this from data after processing traces
    # This saves a lot of time

    return data
