const electron       = nodeRequire('electron');
const showOpenDialog = electron.remote.dialog.showOpenDialog
const browserWindow  = electron.remote.getCurrentWindow();
const os             = nodeRequire('os');
const path           = nodeRequire('path');

class Save {
	constructor() {
		if (config.has('save_directory')) {
			this.directory = config.get('save_directory');
		}
		else {
			this.directory = path.join(os.homedir(), "Documents", "TestAutomation")
		}
		this.initProperty('globalLimit',    'global-limit');
		this.initProperty('snpFiles',       'snp-files');
		this.initProperty('csvFiles',       'csv-files');
		this.initProperty('screenshots',    'screenshots');
		this.initProperty('perTestLimits',  'per-test-limits');
		this.initProperty('markers',        'markers');
		this.initProperty('htmlSummary',    'html-summary');
		this.initProperty('resultsJson',    'results-json');
		this.initProperty('organizeByFile', 'organize-by-file');
		this.initProperty('projectCsv',     'project-csv');
	}

	get directory() {
		return config.get("save_directory");
	}
	set directory(path) {
		if (path) {
			config.set("save_directory", path);
			$('#save-dir-input').val(path);
		}
	}
	showDirectoryDialog() {
		var options = {
			defaultPath: this.directory,
			properties: ['openDirectory']
		};
		return showOpenDialog(browserWindow, options);
	}
	getDirectory() {
		var result = this.showDirectoryDialog();
		if (result && result.length) {
			this.directory = result[0];
		}
	}

	get globalLimit() {
		return $('#global-limit').checked;
	}
	set globalLimit(checked) {
		config.set('global-limit', checked);
		$('#global-limit').checked = checked;
		this.updateSelectAll();
	}

	get snpFiles() {
		return $('#snp-files').checked;
	}
	set snpFiles(checked) {
		config.set('snp-files', checked);
		$('#snp-files').checked = checked;
			this.updateSelectAll();
	}

	get csvFiles() {
		return $('#csv-files').checked;
	}
	set csvFiles(checked) {
		config.set('csv-files', checked);
		$('#csv-files').checked = checked;
		this.updateSelectAll();
	}

	get screenshots() {
		return $('#screenshots').checked;
	}
	set screenshots(checked) {
		config.set('screenshots', checked);
		$('#screenshots').checked = checked;
		this.updateSelectAll();
	}

	get perTestLimits() {
		return $('#per-test-limits').checked;
	}
	set perTestLimits(checked) {
		config.set('per-test-limits', checked);
		$('#per-test-limits').checked = checked;
		this.updateSelectAll();
	}

	get markers() {
		return $('#markers').checked;
	}
	set markers(checked) {
		config.set('markers', checked);
		$('#markers').checked = checked;
		this.updateSelectAll();
	}

	get htmlSummary() {
		return $('#html-summary').checked;
	}
	set htmlSummary(checked) {
		config.set('html-summary', checked);
		$('#html-summary').checked = checked;
		this.updateSelectAll();
	}

	get resultsJson() {
		return $('#results-json').checked;
	}
	set resultsJson(checked) {
		config.set('results-json', checked);
		$('#results-json').checked = checked;
		this.updateSelectAll();
	}

	get organizeByFile() {
		return $('#organize-by-file').checked;
	}
	set organizeByFile(checked) {
		config.set('organize-by-file', checked);
		$('#organize-by-file').checked = checked;
		this.updateSelectAll();
	}

	get projectCsv() {
		return $('#project-csv').checked;
	}
	set projectCsv(checked) {
		config.set('project-csv', checked);
		$('#project-csv').checked = checked;
		this.updateSelectAll();
	}

	get isAllSelected() {
		return this.globalLimit    &&
			   this.snpFiles       &&
			   this.csvFiles       &&
			   this.screenshots    &&
			   this.perTestLimits  &&
			   this.markers        &&
			   this.htmlSummary    &&
			   this.resultsJson    &&
			   this.organizeByFile &&
			   this.projectCsv;
	}
	get selectAll() {
		return $('#select-all').checked;
	}
	set selectAll(checked) {
		this.globalLimit    = checked;
		this.snpFiles       = checked;
		this.csvFiles       = checked;
		this.screenshots    = checked;
		this.perTestLimits  = checked;
		this.markers        = checked;
		this.htmlSummary    = checked;
		this.resultsJson    = checked;
		this.organizeByFile = checked;
		this.projectCsv     = checked;
		$('#select-all').checked = checked;
	}
	updateSelectAll() {
		$('#select-all').checked = this.isAllSelected;
	}

	initProperty(name, key) {
		if (config.has(key)) {
			this[name] = config.get(key);
		}
	}

	toJSON() {
		return {
			"directory":                 this.directory,
			"disable global limit":     !this.globalLimit,
			"disable touchstone files": !this.snpFiles,
			"disable trace csv files":  !this.csvFiles,
			"disable screenshots":      !this.screenshots,
			"disable per-test limits":  !this.perTestLimits,
			"disable markers":          !this.markers,
			"disable html summary":     !this.htmlSummary,
			"disable results json":     !this.resultsJson,
			"organize by file":          this.organizeByFile,
			"enable project csv":        this.projectCsv
		};
	}
}

class Instrument {
	constructor() {
		if (config.has('address')) {
			this.address = config.get('address');
		}
	}

	get connectionType() {
		return 'tcpip';
	}

	get address() {
		var addr = $('#address').val();
		config.set('address', addr)
		return addr;
	}
	set address(addr) {
		config.set('address', addr);
		$('#address').val(addr);
	}

	toJSON() {
		return {
			"connection type": this.connectionType,
			"address":         this.address
		};
	}
}

class Settings {
	constructor() {
		this.instrument = new Instrument();
		this.save = new Save();
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

	summaryUrl() {
		if (!save.htmlSummary) {
			return '';
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

	toJSON() {
		return {
			"serial no": this.serialNo,
			"instrument": this.instrument.toJSON(),
			"save":       this.save.toJSON()
		};
	}
}

module.exports = new Settings();
