const consoleDisplay = window.nodeRequire(path.resolve(root_path, 'console-display'));
const resultsDisplay = window.nodeRequire(path.resolve(root_path, 'results-display'));

class Display {
  constructor() {
    this.console = consoleDisplay;
    this.results = resultsDisplay;
  }
  showConsole() {
    this.results.hide();
    this.console.show();
  }
  showResults(display) {
    this.console.hide();
    this.results.show(display);
  }
  hide() {
    this.console.hide();
    this.results.hide();
  }
}

module.exports = new Display();
