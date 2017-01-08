from   rohdeschwarz.general     import format_value
from   wheezy.template.engine   import Engine
from   wheezy.template.ext.core import CoreExtension
from   wheezy.template.loader   import FileLoader
import base64
from   collections				 import OrderedDict
from   pathlib     				 import Path

def check_test_info(ti):
	if not "dut noun" in ti:
		ti["dut noun"] = "DUT"
	if not "serial number" in ti:
		ti["serial number"] = "__abc__"
	return ti

def generate(filename, test_info, data):
	check_test_info(test_info)
	path = Path(__file__).parent / 'views'
	searchpath = [str(path)]
	engine = Engine(
		loader=FileLoader(searchpath),
		extensions=[CoreExtension()]
	)
	engine.global_vars.update({'format_value': format_value})
	template = engine.get_template('template.html')
	with open(filename, 'w') as f:
		f.write(template.render({'data': data, 'test_info': test_info}))

#
