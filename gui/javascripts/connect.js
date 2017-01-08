function connect() {
	controls.disableConnect();
	results.hide();
	div_console.clear();
	div_console.show();

	rstest_bin = path.resolve(root_path, '../rstest/run');
	if (process.platform == "win32") {
		rstest_bin = rstest_bin + ".exe";
	}
	var _process = spawn(rstest_bin, [controls.ipAddress()]);
	_process.stdout.on('data', div_console.print);
	_process.on('close', connectClosed);
}
function connectClosed(code) {
	if (code == 0) {
		controls.enableMeasure();
		controls.showMeasure();
	}
	else {
		div_console.print(`child process exited with code ${code}`);
		controls.enableConnect();
		// Display warning!
	}
}
$('#connect').on('click', connect);
