import os
from   collections  import OrderedDict
from   rstest.general import make_path_safe

def process_trace(path, trace, settings):
    trc_name = trace.name

    # Data (csv) files
    data = OrderedDict()
    path.cd_trace(trc_name)
    if not settings['save']['disable trace csv files']:
        path.mkdirs()
        filename = path.file_path(trc_name, '.csv')
        if trace.time_domain.on:
            data["time domain"] = True
            trace.save_data_locally(filename)
        else:
            trace.save_complex_data_locally(filename)
        print("{0}.csv".format(trc_name), flush=True)

    if trace.limits.on:
        if trace.limits.passed:
            data["limits"] = "passed"
        else:
            data["limits"] = "failed"
    data['markers'] = OrderedDict()
    for i in trace.markers:
        m    = trace.marker(i)
        name = m.name
        data['markers'][name] = OrderedDict()
        x = OrderedDict()
        x['value'] = m.x
        x['units'] = str(trace.x_units())
        y = OrderedDict()
        y['value'] = m.y
        y['units'] = str(trace.y_units())
        data['markers'][name]['x'] = x
        data['markers'][name]['y'] = y
    return data
