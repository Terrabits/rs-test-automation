const spawn = window.nodeRequire('child_process').spawn;

function connect(address, stdout, onclose) {
	rstest_bin = path.resolve(root_path, '../rstest/run');
	if (process.platform == "win32") {
		rstest_bin = rstest_bin + ".exe";
	}
	var env = Object.create(process.env);
  env.PYTHONIOENCODING = 'utf-8';
  env.LANG             = "en_US.UTF-8";
  options = {env: env, encoding: 'utf8'};
	var _process = spawn(rstest_bin, [address], options);
	_process.stdout.on('data', stdout);
	_process.on('close', onclose);
}

module.exports = connect;
