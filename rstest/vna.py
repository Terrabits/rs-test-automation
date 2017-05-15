from collections  import OrderedDict
from rstest.general import touch, print_check

def process_vna(path, vna, settings):
    data = OrderedDict()
    if not settings.is_save_vna():
        return data

    path.cd_vna_screenshot()
    if not settings['save']['disable screenshots']:
        path.mkdirs()
        filename = path.file_path("screenshot", ".png")
        print("Screenshot          ", end='', flush=True)
        vna.save_screenshot_locally(filename, "PNG")
        print_check()
    if not settings['save']['disable global limit'] and vna.is_limits():
        print("Global limit        ", end='', flush=True)
        path.cd_vna_limits()
        path.mkdirs()
        if vna.passed:
            data["limits"] = "passed"
            touch(path.file_path("", "__PASSED__"))
        else:
            data["limits"] = "failed"
            touch(path.file_path("", "__FAILED__"))
        print_check()
    return data
