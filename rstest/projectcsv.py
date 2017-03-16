import csv
from   os.path import isfile


headers = []
row     = []

def clear():
	headers = []
	row     = []

def add(header, value):
	headers.append(header)
	row.append(value)

def generate(filename, serial_no, data):
	clear()
	add("serial no", serial_no)
	if not 'limits' in data and not 'diagrams' in data:
		return
	if 'limits' in data:
		add("global limits", data['limits'])
	for diag_name in data['diagrams']:
		diag = data['diagrams'][diag_name]
		if 'limits' in diag:
			label = "{0} limits".format(diag_name)
			add(label, diag['limits'])
		if 'skew' in diag:
			label = "{0} (s)".format(diag_name)
			add(label, diag['skew'])
		if 'prop delay' in diag:
			label = "{0} (s)".format(diag_name)
			add(label, diag['prop delay'])
		for trc_name in diag['traces']:
			trc = diag['traces'][trc_name]
			if 'limits' in trc:
				label = "{0} - {1} limits".format(diag_name, trc_name)
				add(label, trc['limits'])
			if 'markers' in trc:
				for mkr_name in trc['markers']:
					mkr = trc['markers'][mkr_name]
					x_label = "{0} - {1} {2} X ({3})".format(diag_name, trc_name, mkr_name, mkr['x']['units'])
					y_label = "{0} - {1} {2} Y ({3})".format(diag_name, trc_name, mkr_name, mkr['y']['units'])
					add(x_label, mkr['x']['value'])
					add(y_label, mkr['y']['value'])

	if not isfile(filename):
		with open(filename, 'w', newline='') as f:
			csvwriter = csv.writer(f)
			csvwriter.writerow(headers)
	with open(filename, 'a', newline='') as f:
		csvwriter = csv.writer(f)
		csvwriter.writerow(row)
