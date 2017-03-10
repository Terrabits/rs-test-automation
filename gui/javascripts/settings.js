function box(id) {
	return document.getElementById(id);
}

class Settings {
	get globalLimit() {
		return box('global-limit').checked;
	}
	set globalLimit(checked) {
		box('global-limit').checked = checked;
	}

	get snpFiles() {
		return box('snp-files').checked;
	}
	set snpFiles(checked) {
		box('snp-files').checked = checked;
	}

	get csvFiles() {
		return box('csv-files').checked;
	}
	set csvFiles(checked) {
		box('csv-files').checked = checked;
	}

	get screenshots() {
		return box('screenshots').checked;
	}
	set screenshots(checked) {
		box('screenshots').checked = checked;
	}

	get perTestLimits() {
		return box('per-test-limits').checked;
	}
	set perTestLimits(checked) {
		box('per-test-limits').checked = checked;
	}

	get markers() {
		return box('markers').checked;
	}
	set markers(checked) {
		box('markers').checked = checked;
	}

	get htmlSummary() {
		return box('html-summary').checked;
	}
	set htmlSummary(checked) {
		box('html-summary').checked = checked;
	}

	get resultsJson() {
		return box('results-json').checked;
	}
	set resultsJson(checked) {
		box('results-json').checked = checked;
	}

	get organizeByFile() {
		return box('organize-by-file').checked;
	}
	set organizeByFile(checked) {
		box('organize-by-file').checked = checked;
	}

	get projectCsv() {
		return box('project-csv').checked;
	}
	set projectCsv(checked) {
		box('project-csv').checked = checked;
	}

	toJSON() {
		return {
			"directory":                "~/Documents/TestAutomation/",
			"disable global limit":     !this.globalLimit,
			"disable touchstone files": !this.snpFiles,
			"disable trace csv files":  !this.csvFiles,
			"disable screenshots":      !this.screenshots,
			"disable per-test limits":  !this.perTestLimits,
			"disable markers":          !this.markers,
			"disable html summary":     !this.htmlSummary,
			"disable results json":     !this.resultsJson,
			"organize by file":         this.organizeByFile,
			"enable project csv":       this.projectCsv
		};
	}
}
module.exports = new Settings()
