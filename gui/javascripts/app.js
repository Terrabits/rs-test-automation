const onConnectClicked    = window.nodeRequire(path.resolve(root_path, 'on-connect-clicked'));
const onMeasureClicked    = window.nodeRequire(path.resolve(root_path, 'on-measure-clicked'));
const onDisconnectClicked = window.nodeRequire(path.resolve(root_path, 'on-disconnect-clicked'));

// Settings callbacks
$('#display-results' ).on('change', function() {
  settings.display.results = this.value;
  if (display.results.shown) {
    display.showResults(this.value);
  }
});
$('#save-dir-button' ).on('click',  function() {settings.save.getDirectory();               });
$('#select-all'      ).on('change', function() {settings.save.selectAll      = this.checked;});
$('#global-limit'    ).on('change', function() {settings.save.globalLimit    = this.checked;});
$('#snp-files'       ).on('change', function() {settings.save.snpFiles       = this.checked;});
$('#csv-files'       ).on('change', function() {settings.save.csvFiles       = this.checked;});
$('#screenshots'     ).on('change', function() {settings.save.screenshots    = this.checked;});
$('#per-test-limits' ).on('change', function() {settings.save.perTestLimits  = this.checked;});
$('#markers'         ).on('change', function() {settings.save.markers        = this.checked;});
$('#html-summary'    ).on('change', function() {settings.save.htmlSummary    = this.checked;});
$('#results-json'    ).on('change', function() {settings.save.resultsJson    = this.checked;});
$('#organize-by-file').on('change', function() {settings.save.organizeByFile = this.checked;});
$('#project-csv'     ).on('change', function() {settings.save.projectCsv     = this.checked;});

// Controls
$('#connect-button').on('click', onConnectClicked);
$('#measure-button').on('click', onMeasureClicked);
$('#disconnect-button').on('click', onDisconnectClicked)

if (settings.instrument.address) {
  onConnectClicked();
}
