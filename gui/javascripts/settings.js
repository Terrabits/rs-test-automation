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
			globalLimit: this.globalLimit,
			snpFiles: this.snpFiles,
			csvFiles: this.csvFiles,
			screenshots: this.screenshots,
			perTestLimits: this.perTestLimits,
			markers: this.markers,
			htmlSummary: this.htmlSummary,
			resultsJson: this.resultsJson,
			organizeByFile: this.organizeByFile,
			projectCsv: this.projectCsv
		};
	}
}
module.exports = new Settings()
