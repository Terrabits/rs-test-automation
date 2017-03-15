const fullResults   = window.nodeRequire(path.resolve(root_path, 'full-results-display'));
const simpleResults = window.nodeRequire(path.resolve(root_path, 'simple-results-display'));

class ResultsDisplay {
  constructor() {
    this.full   = fullResults;
    this.simple = simpleResults;
  }
  get shown() {
    if (this.full.shown) {
      return "full";
    }
    if (this.simple.shown) {
      return "simple";
    }
    return false;
  }
  show(display) {
    if (display.toLowerCase() == "simple") {
      this.full.hide();
      this.simple.show();
    }
    else {
      this.simple.hide();
      this.full.show();
    }
    $('div#results').removeClass('hide');
  }
  hide() {
    this.full.hide();
    this.simple.hide();
    $('div#results').addClass('hide');
  }
  update(serialNo, htmlSummaryPath, data) {
    this.simple.add(serialNo, data);
    this.full.url = htmlSummaryPath;
  }
}
module.exports = new ResultsDisplay();
