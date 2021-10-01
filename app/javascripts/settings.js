const InstrumentSettings = window.nodeRequire(path.resolve(root_path, 'instrument-settings'));
const DisplaySettings    = window.nodeRequire(path.resolve(root_path, 'display-settings'));
const SaveSettings       = window.nodeRequire(path.resolve(root_path, 'save-settings'));

class Settings {
	constructor() {
		this.instrument = new InstrumentSettings();
		this.display    = new DisplaySettings();
		this.save       = new SaveSettings();
	}
	get serialNo() {
		return $('#serial-no').val();
	}
	set serialNo(value) {
		$('#serial-no').val(value);
	}
	clearSerialNo() {
		this.serialNo = '';
	}

	htmlSummaryPath() {
		if (!this.save.htmlSummary) {
			return './404.html';
		}
		var root_path  = this.save.directory;
    if (this.save.organizeByFile) {
      var filename = this.serialNo + ".html";
      return path.join(root_path, "summary", filename);
    }
    else {
      var filename = "summary.html";
      return path.join(root_path, this.serialNo, filename);
    }
	}

	resultsJsonPath() {
		if (!this.save.resultsJson) {
			return '';
		}
		var root_path  = this.save.directory;
    if (this.save.organizeByFile) {
      var filename = this.serialNo + ".json";
      return path.join(root_path, "json", filename);
    }
    else {
      var filename = "summary.json";
      return path.join(root_path, this.serialNo, filename);
    }
	}

	toJSON() {
		return {
			"serial no": this.serialNo,
			"instrument": this.instrument.toJSON(),
			"save":       this.save.toJSON()
		};
	}
}

module.exports = new Settings();
