window.nodeRequire = require;
window.nodeExports = window.exports;
window.nodeModule  = window.module;
delete window.require;
delete window.exports;
delete window.module;

const path        = window.nodeRequire('path');
var root_path     = path.resolve(__dirname, 'javascripts/')
const div_console = window.nodeRequire(path.resolve(root_path, 'div_console'));
const results     = window.nodeRequire(path.resolve(root_path, 'iframe_results'));
const controls    = window.nodeRequire(path.resolve(root_path, 'controls'));
const spawn       = window.nodeRequire('child_process').spawn;
const os          = window.nodeRequire('os')
