const spawn = require('child_process').spawn;

function measure() {
  bin = "/Users/nicholaslalic/Documents/Python/rs-test-automation/app/rstest/run";
  options = {encoding: 'utf8'};
	var _process = spawn(bin, ["127.0.0.1"], options);
  var print_data = (data) => { console.log(String(data)); };
	_process.stdout.on('data', print_data);
  var onclose = (code) => { console.log(code); };
	_process.on('close', onclose);
}

module.exports = measure;
