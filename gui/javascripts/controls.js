const connect  = window.nodeRequire(path.resolve(root_path, 'connect-controls'));
const measure  = window.nodeRequire(path.resolve(root_path, 'measure-controls'));
const settings = window.nodeRequire(path.resolve(root_path, 'settings-controls'));

class Controls {
  constructor() {
    this.connect  = connect;
    this.measure  = measure;
    this.settings = settings;
  }
  showConnect() {
    this.measure.hide();
    this.connect.show();
    this.settings.close();
  }
  showMeasure() {
    this.connect.hide();
    this.measure.show();
    this.settings.close();
  }
  enable() {
    this.connect.enable();
    this.measure.enable();
    this.settings.enable();
  }
  disable() {
    this.connect.disable();
    this.measure.disable();
    this.settings.disable();
  }
}

module.exports = new Controls();
