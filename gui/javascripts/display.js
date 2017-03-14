const consoleDisplay = window.nodeRequire(path.resolve(root_path, 'console-display'));
const results        = window.nodeRequire(path.resolve(root_path, 'results'));

class Display {
  constructor() {
    this.console = consoleDisplay;
    this.results = results;
  }
  showConsole() {
    this.results.hide();
    this.console.show();
  }
  showResults() {
    this.console.hide();
    this.results.show();
  }
  hide() {
    this.console.hide();
    this.results.hide();
  }
}

module.exports = new Display();
