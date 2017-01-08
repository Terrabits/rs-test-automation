function measure() {
  controls.disableMeasure();
  results.hide();
  div_console.clear();
  div_console.show();


  rstest_bin = path.resolve(root_path, '../rstest/run');
  if (process.platform == "win32") {
    rstest_bin = rstest_bin + ".exe";
  }
	var _process = spawn(rstest_bin, [controls.ipAddress(), controls.serialNumber()]);
	_process.stdout.on('data', div_console.printAndScroll);
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
    // Display warning!
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
