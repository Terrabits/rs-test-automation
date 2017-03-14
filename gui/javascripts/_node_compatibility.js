// Move node methods
// Make room for JQuery, etc
window.nodeRequire = require;
window.nodeExports = window.exports;
window.nodeModule  = window.module;
delete window.require;
delete window.exports;
delete window.module;

// Save application state
const ElectronConfig = window.nodeRequire('electron-config');
const config         = new ElectronConfig();

// node modules
const os             = window.nodeRequire('os');
const path           = window.nodeRequire('path');

// js root path
var   root_path      = path.resolve(__dirname, 'javascripts/')
function projectRequire(js) { // ?
  return window.nodeRequire(path.resolve(root_path, js));
}
