const electron       = nodeRequire('electron');
const showOpenDialog = electron.remote.dialog.showOpenDialog
const browserWindow  = electron.remote.getCurrentWindow();

function box(id) {
	return document.getElementById(id);
}

class Save {
	constructor() {
		if (config.has('save_directory')) {
			this.directory = config.get('save_directory');
		}
		else {
			this.directory = "~/Documents/TestAutomation";
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
			box('save-dir-input').value = path;
		}
	}
	showDirectoryDialog() {
		var options = {
			defaultpath: this.directory,
			properties: ['openDirectory']
		};
		return showOpenDialog(browserWindow, options);
	}
	getDirectory() {
		var result = this.showDirectoryDialog();
		if (result.length) {
			this.directory = result[0];
		}
	}

	get globalLimit() {
		return box('global-limit').checked;
	}
	set globalLimit(checked) {
		config.set('global-limit', checked);
		box('global-limit').checked = checked;
		this.updateSelectAll();
	}

	get snpFiles() {
		return box('snp-files').checked;
	}
	set snpFiles(checked) {
		config.set('snp-files', checked);
		box('snp-files').checked = checked;
			this.updateSelectAll();
	}

	get csvFiles() {
		return box('csv-files').checked;
	}
	set csvFiles(checked) {
		config.set('csv-files', checked);
		box('csv-files').checked = checked;
		this.updateSelectAll();
	}

	get screenshots() {
		return box('screenshots').checked;
	}
	set screenshots(checked) {
		config.set('screenshots', checked);
		box('screenshots').checked = checked;
		this.updateSelectAll();
	}

	get perTestLimits() {
		return box('per-test-limits').checked;
	}
	set perTestLimits(checked) {
		config.set('per-test-limits', checked);
		box('per-test-limits').checked = checked;
		this.updateSelectAll();
	}

	get markers() {
		return box('markers').checked;
	}
	set markers(checked) {
		config.set('markers', checked);
		box('markers').checked = checked;
		this.updateSelectAll();
	}

	get htmlSummary() {
		return box('html-summary').checked;
	}
	set htmlSummary(checked) {
		config.set('html-summary', checked);
		box('html-summary').checked = checked;
		this.updateSelectAll();
	}

	get resultsJson() {
		return box('results-json').checked;
	}
	set resultsJson(checked) {
		config.set('results-json', checked);
		box('results-json').checked = checked;
		this.updateSelectAll();
	}

	get organizeByFile() {
		return box('organize-by-file').checked;
	}
	set organizeByFile(checked) {
		config.set('organize-by-file', checked);
		box('organize-by-file').checked = checked;
		this.updateSelectAll();
	}

	get projectCsv() {
		return box('project-csv').checked;
	}
	set projectCsv(checked) {
		config.set('project-csv', checked);
		box('project-csv').checked = checked;
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
		return box('select-all').checked;
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
		box('select-all').checked = checked;
	}
	updateSelectAll() {
		box('select-all').checked = this.isAllSelected;
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

var save = new Save();
$(box('select-all'      )).on('change', function() {save.selectAll      = this.checked;});
$(box('global-limit'    )).on('change', function() {save.globalLimit    = this.checked;});
$(box('snp-files'       )).on('change', function() {save.snpFiles       = this.checked;});
$(box('csv-files'       )).on('change', function() {save.csvFiles       = this.checked;});
$(box('screenshots'     )).on('change', function() {save.screenshots    = this.checked;});
$(box('per-test-limits' )).on('change', function() {save.perTestLimits  = this.checked;});
$(box('markers'         )).on('change', function() {save.markers        = this.checked;});
$(box('html-summary'    )).on('change', function() {save.htmlSummary    = this.checked;});
$(box('results-json'    )).on('change', function() {save.resultsJson    = this.checked;});
$(box('organize-by-file')).on('change', function() {save.organizeByFile = this.checked;});
$(box('project-csv'     )).on('change', function() {save.projectCsv     = this.checked;});

var settings   = {save: save};
module.exports = settings;
