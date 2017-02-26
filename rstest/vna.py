from collections  import OrderedDict
from rstest.general import touch

def process_vna(path, vna, settings):
    path.cd_vna_screenshot()
    if not settings['save']['disable screenshots']:
        path.mkdirs()
        filename = path.file_path("screenshot", ".png")
        print("vna screenshot", flush=True)
        vna.save_screenshot_locally(filename, "PNG")

    data = OrderedDict()
    if vna.is_limits():
        path.cd_vna_limits()
        path.mkdirs()
        if vna.passed:
            data["limits"] = "passed"
            touch(path.file_path("", "__PASSED__"))
        else:
            data["limits"] = "failed"
            touch(path.file_path("", "__FAILED__"))
    return data
