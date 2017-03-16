import os
from   collections  import OrderedDict
from   rstest.general import make_path_safe

def process_trace(path, trace, settings):
    data = OrderedDict()

    # Data (csv) files
    trc_name = trace.name
    path.cd_trace(trc_name)
    if not settings['save']['disable trace csv files']:
        path.mkdirs()
        filename = path.file_path(trc_name, '.csv')
        print("{0}.csv".format(trc_name), flush=True)
        if trace.time_domain.on:
            data["time domain"] = True
            trace.save_data_locally(filename)
        else:
            trace.save_complex_data_locally(filename)


    # Limits
    if not settings['save']['disable per-test limits']:
        print("{0} limits".format(trc_name), flush=True)
        if trace.limits.on:
            if trace.limits.passed:
                data["limits"] = "passed"
            else:
                data["limits"] = "failed"

    # Markers
    if not settings['save']['disable markers']:
        markers_data = data['markers'] = OrderedDict()
        for i in trace.markers:
            m    = trace.marker(i)
            name = m.name
            print("Processing {0}".format(name), flush=True)
            marker_data = markers_data[name] = OrderedDict()
            x = OrderedDict()
            x['value'] = m.x
            x['units'] = str(trace.x_units())
            y = OrderedDict()
            y['value'] = m.y
            y['units'] = str(trace.y_units())
            marker_data['x'] = x
            marker_data['y'] = y
    return data
