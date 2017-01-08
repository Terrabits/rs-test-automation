R&S Test Automation
===================

Connects to a Rohde & Schwarz Vector Network Analyzer (VNA), runs all sweeps, then saves the following data:

- Screenshot
- Touchstone files
- Global pass/fail
- Diagram images
- trace data (csv)
- marker positions and values
- skew, propagation delay (if indicated)
- Diagram pass/fail

Data is saved to the `~/Documents/TestAutomation` folder, organized by DUT serial number. The data for each dut is organized by diagram (test).

Requirements
------------

- Python 3.x
- Node 6.9+
- Ruby 2.2+
- Bundler Ruby gem

The following packages and modules are primarily used:

The python [rohdeschwarz](https://github.com/Terrabits/rohdeschwarz) package is used to control the VNA.

[wheezy.template](https://pypi.python.org/pypi/wheezy.template) is used to generate the `summary.html` for each test on-the-fly.

[Middleman 4](https://middlemanapp.com/) is used to generate the static ui files (html, css, js).

[electron](http://electron.atom.io/) is used to host the html/css/js ui. Node is used to orchestrate the tests in python via `child_process`es.

[electron-builder](https://github.com/electron-userland/electron-builder) is used to create a distributable / installer.

Installation
------------

Assuming Python, Node and Ruby are installed, you can get setup by typing:

```bash
cd path/to/project
pip install -r requirements.txt
npm install
bundle install
```

Development
-----------

The following scripts are available from the command line:

### Build `gui` source with Middleman

`npm run build-mm`

### Build python code with pyinstaller

`npm run build-py`

### Pack and distribute

The following commands assume the python and gui sources have been built successfully.

To pack files into a single folder (`dist/*-unpacked`):

`npm run pack`

To create a distributable installer:

`npm dist`

See the [electron-builder](https://github.com/electron-userland/electron-builder) project for more details on how the installer is generated.

From the command line
---------------------

If you'd prefer, you can separate out the user interface (node, electron, ruby, middleman) and stick to python and the command line. In that case, you only need the following sources:

- `rstest/`
- `test/` (optional)
- `run.py`
- `requirements.txt`
- `run.spec`

The `run.py` script has the following modes of operation:

### With no args

The script will ask you for the VNA ip address, then ask you for the serial number of your first DUT. After each measurement you will be prompted to continue (measure next DUT) or quit.

### Test VNA connection

If you execute the run.py script with the IP address as a command line argument, the script will attempt to connect to the VNA and report back whether or not it could connect and what it connected to.

### Measure one DUT

With the following command line structure the script will measure a single DUT then return:

`run.py <ip address> <serial number>`

Results
-------

Test results can be found in the `~/Documents/TestAutomation` folder.