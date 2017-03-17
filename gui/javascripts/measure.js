const spawn = window.nodeRequire('child_process').spawn;

function measure(serialNo, settingsJson, stdout, stderr, onclose) {
  rstest_bin = path.resolve(root_path, '../rstest/run');
  if (process.platform == "win32") {
    rstest_bin = rstest_bin + ".exe";
  }
  var env = Object.create(process.env);
  env.PYTHONIOENCODING = 'utf-8';
  env.LANG             = "en_US.UTF-8";
  options = {env: env, encoding: 'utf8'};
	var _process = spawn(rstest_bin, [serialNo, settingsJson], options);
	_process.stdout.on('data', stdout);
  _process.stderr.on('data', stderr);
	_process.on('close', onclose);
}

module.exports = measure;
