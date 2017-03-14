const connect = window.nodeRequire(path.resolve(root_path, 'connect'));

function onConnectClicked() {
	alert.hide();

	if (!settings.instrument.address) {
		alert.showMessage("Please enter instrument address to continue");
		alert.show();
		controls.enable();
		return;
	}

	var stdout = (text) => {
		display.console.print(text);
		display.console.scrollDown();
	};
	var onclose = (code) => {
		controls.enable();
		if (code != 0) {
			alert.showMessage("*Error connecting to VNA");
		}
		else {
			controls.showMeasure();
		}
	};

	controls.disable();
	display.console.clear();
	display.showConsole();
	connect(settings.instrument.address, stdout, onclose);
}

module.exports = onConnectClicked;
