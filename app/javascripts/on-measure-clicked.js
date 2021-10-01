const measure = window.nodeRequire(path.resolve(root_path, 'measure'));
const fs      = window.nodeRequire('fs');

var stderr = '';
function onstderr(text) {
  stderr += text;
}
function onstdout(text) {
  display.console.print(text);
  display.console.scrollDown();
}

function onclose(code) {
  if (code == 0) {
    // Success
    var data = {};
    if (settings.save.resultsJson) {
      data = JSON.parse(fs.readFileSync(settings.resultsJsonPath()));
    }
    display.results.update(settings.serialNo, settings.htmlSummaryPath(), data);
    if (settings.display.results == "full") {
      if (!settings.save.htmlSummary) {
        settings.display.results = "simple";
      }
    }
    display.showResults(settings.display.results);
    settings.clearSerialNo();
  }
  else {
    // Failure
    display.console.print("\n*** PYTHON ERROR ***\n\n");
    display.console.print(stderr);
    display.console.scrollDown();
    alert.showMessage("Measurement error. See console below for more details.");
    display.showConsole();
  }
  controls.enable();
}

function onMeasureClicked() {
  alert.hide();
  controls.settings.close();
  if (!settings.serialNo) {
    alert.showMessage('Please provide serial number');
    return;
  }
  controls.disable();
	display.console.clear();
	display.showConsole();
  measure(settings.serialNo, JSON.stringify(settings), onstdout, onstderr, onclose);
}

module.exports = onMeasureClicked;
