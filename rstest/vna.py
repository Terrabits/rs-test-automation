from collections  import OrderedDict
from rstest.general import touch

def process_vna(path, vna):
    # print("screenshot.png", flush=True)
    # vna.save_screenshot_locally(str(path / 'screenshot'), "PNG")
    data = OrderedDict()
    if vna.is_limits():
        if vna.passed:
            data["limits"] = "passed"
            touch(str(path / "__PASSED__"))
        else:
            data["limits"] = "failed"
            touch(str(path / "__FAILED__"))
    return data
