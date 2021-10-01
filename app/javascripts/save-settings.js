const remote         = require('@electron/remote');
const browserWindow  = remote.getCurrentWindow();
const showOpenDialog = remote.dialog.showOpenDialog

const os             = nodeRequire('os');
const path           = nodeRequire('path');

class SaveSettings {
	constructor() {
		if (config.has('save-directory')) {
			this.directory = config.get('save-directory');
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
		return config.get("save-directory");
	}
	set directory(path) {
		if (path) {
			config.set("save-directory", path);
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
		return $('#global-limit').prop('checked');
	}
	set globalLimit(checked) {
		config.set('global-limit', checked);
		$('#global-limit').prop('checked', checked);
		this.updateSelectAll();
	}

	get snpFiles() {
		return $('#snp-files').prop('checked');
	}
	set snpFiles(checked) {
		config.set('snp-files', checked);
		$('#snp-files').prop('checked', checked);
			this.updateSelectAll();
	}

	get csvFiles() {
		return $('#csv-files').prop('checked');
	}
	set csvFiles(checked) {
		config.set('csv-files', checked);
		$('#csv-files').prop('checked', checked);
		this.updateSelectAll();
	}

	get screenshots() {
		return $('#screenshots').prop('checked');
	}
	set screenshots(checked) {
		config.set('screenshots', checked);
		$('#screenshots').prop('checked', checked);
		this.updateSelectAll();
	}

	get perTestLimits() {
		return $('#per-test-limits').prop('checked');
	}
	set perTestLimits(checked) {
		config.set('per-test-limits', checked);
		$('#per-test-limits').prop('checked', checked);
		this.updateSelectAll();
	}

	get markers() {
		return $('#markers').prop('checked');
	}
	set markers(checked) {
		config.set('markers', checked);
		$('#markers').prop('checked', checked);
		this.updateSelectAll();
	}

	get htmlSummary() {
		return $('#html-summary').prop('checked');
	}
	set htmlSummary(checked) {
		config.set('html-summary', checked);
		$('#html-summary').prop('checked', checked);
		this.updateSelectAll();
	}

	get resultsJson() {
		return $('#results-json').prop('checked');
	}
	set resultsJson(checked) {
		config.set('results-json', checked);
		$('#results-json').prop('checked', checked);
		this.updateSelectAll();
	}

	get organizeByFile() {
		return $('#organize-by-file').prop('checked');
	}
	set organizeByFile(checked) {
		config.set('organize-by-file', checked);
		$('#organize-by-file').prop('checked', checked);
		this.updateSelectAll();
	}

	get projectCsv() {
		return $('#project-csv').prop('checked');
	}
	set projectCsv(checked) {
		config.set('project-csv', checked);
		$('#project-csv').prop('checked', checked);
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
		return $('#select-all').prop('checked');
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
		$('#select-all').prop('checked', checked);
	}
	updateSelectAll() {
		$('#select-all').prop('checked', this.isAllSelected);
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

module.exports = SaveSettings;
