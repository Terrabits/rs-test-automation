

var _stderr_read = '';
function readStderr(data) {
  console.log("stderr: #{data}");
  _stderr_read = _stderr_read + data;
}

var _process;
function measure() {
  controls.disableMeasure();
  results.hide();
  div_console.clear();
  div_console.show();

  rstest_bin = path.resolve(root_path, '../rstest/run');
  if (process.platform == "win32") {
    rstest_bin = rstest_bin + ".exe";
  }
	_process = spawn(rstest_bin, [controls.ipAddress(), controls.serialNumber()]);
	_process.stdout.on('data', div_console.printAndScroll);
  _process.stderr.on('data', readStderr);
	_process.on('close', measureClosed);
}
function measureClosed(code) {
  controls.enableMeasure();
  if (code == 0) {
    div_console.hide();

    var url = path.resolve(os.homedir(), 'Documents', 'TestAutomation', controls.serialNumber(), 'summary.html');
    controls.clearSerialNumber();

    results.setUrl(url);
    results.show();
  }
  else {
    div_console.printAndScroll("\n* ERROR!\n")
    div_console.printAndScroll("*   An error occurred and the measurement exited prematurely.\n");
    div_console.printAndScroll("*   Please check your setup and try again.");
    div_console.printAndScroll("*\n");
    div_console.printAndScroll("* Python error:");
    div_console.printAndScroll(_stderr_read);
  }
}
function disconnect() {
  controls.enableConnect();
  controls.showConnect()
  results.hide()
  div_console.hide()
}
$('#measure').on('click', measure);
$('#disconnect').on('click', disconnect)
