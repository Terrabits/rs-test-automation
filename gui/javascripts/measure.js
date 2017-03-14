const spawn = window.nodeRequire('child_process').spawn;

var _stderr_read = '';
function readStderr(data) {
  _stderr_read = _stderr_read + data;
}

var _process;
function measure() {
  controls.disableMeasure();
  results.hide();
  controls.hideAlert();
  div_console.clear();
  div_console.show();

  rstest_bin = path.resolve(root_path, '../rstest/run');
  if (process.platform == "win32") {
    rstest_bin = rstest_bin + ".exe";
  }
	_process = spawn(rstest_bin, [settings.serialNo, settings.toJSON()]);
	_process.stdout.on('data', div_console.printAndScroll);
  _process.stderr.on('data', readStderr);
	_process.on('close', measureClosed);
}
function measureClosed(code) {
  if (code == 0) {
    div_console.hide();
    var saveDir  = settings.save.directory;
    var serialNo = controls.serialNumber();
    var url;
    if (settings.save.organizeByFile) {
      var filename = serialNo + ".html";
      url          = path.join(saveDir, "summary", filename);
    }
    else {
      var filename = "summary.html";
      url          = path.join(saveDir, serialNo, filename);
    }
    controls.clearSerialNumber();
    results.setUrl(url);
    results.show();
  }
  else {
    controls.setAlert("Measurement error. See console below for more details.");
    controls.showAlert();
    div_console.printAndScroll("\n* ERROR!\n")
    div_console.printAndScroll("*   An error occurred and the measurement exited prematurely.\n");
    div_console.printAndScroll("*   Please check your setup and try again.");
    div_console.printAndScroll("*\n");
    div_console.printAndScroll("* Python error:");
    div_console.printAndScroll(_stderr_read);
  }
  controls.enableMeasure();
}
