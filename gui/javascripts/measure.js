const spawn = window.nodeRequire('child_process').spawn;

function measure(serialNo, settingsJson, stdout, stderr, onclose) {
  rstest_bin = path.resolve(root_path, '../rstest/run');
  if (process.platform == "win32") {
    rstest_bin = rstest_bin + ".exe";
  }
	var _process = spawn(rstest_bin, [serialNo, settingsJson]);
	_process.stdout.on('data', stdout);
  _process.stderr.on('data', stderr);
	_process.on('close', onclose);
}

module.exports = measure;
