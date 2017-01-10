// Init
if (config.has('ip-address')) {
	controls.setIpAddress(config.get('ip-address'));
}

function connect() {
	controls.disableConnect();
	results.hide();
	controls.hideAlert();
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
		config.set('ip-address', controls.ipAddress());
	}
	else {
		controls.enableConnect();
		controls.setAlert("Error connecting to VNA");
		controls.showAlert();
	}
}
$('#connect').on('click', connect);
