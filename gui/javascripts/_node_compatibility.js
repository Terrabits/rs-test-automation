// Move node methods
// Make room for JQuery, etc
window.nodeRequire = require;
window.nodeExports = window.exports;
window.nodeModule  = window.module;
delete window.require;
delete window.exports;
delete window.module;

// Node modules
const ElectronConfig = window.nodeRequire('electron-config');
const config         = new ElectronConfig();
const os             = window.nodeRequire('os');
const spawn          = window.nodeRequire('child_process').spawn;

// Project modules
const path        = window.nodeRequire('path');
var   root_path   = path.resolve(__dirname, 'javascripts/')
const controls    = window.nodeRequire(path.resolve(root_path, 'controls'));
const settings    = window.nodeRequire(path.resolve(root_path, 'settings'));
const div_console = window.nodeRequire(path.resolve(root_path, 'div_console'));
const results     = window.nodeRequire(path.resolve(root_path, 'iframe_results'));
