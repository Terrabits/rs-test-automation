const connect = window.nodeRequire(path.resolve(root_path, 'connect-controls'));
const measure = window.nodeRequire(path.resolve(root_path, 'measure-controls'));

class Controls {
  constructor() {
    this.connect = connect;
    this.measure = measure;
  }
  showConnect() {
    this.measure.hide();
    this.connect.show();
  }
  showMeasure() {
    this.connect.hide();
    this.measure.show();
  }
  enable() {
    this.connect.enable();
    this.measure.enable();
  }
  disable() {
    this.connect.disable();
    this.measure.disable();
  }
}

module.exports = new Controls();
