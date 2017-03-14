const spawn = window.nodeRequire('child_process').spawn;

function connect(address, stdout, onclose) {
	rstest_bin = path.resolve(root_path, '../rstest/run');
	if (process.platform == "win32") {
		rstest_bin = rstest_bin + ".exe";
	}
	var _process = spawn(rstest_bin, [address]);
	_process.stdout.on('data', stdout);
	_process.on('close', onclose);
}

module.exports = connect;
