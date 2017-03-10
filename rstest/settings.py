# Settings and Defaults
# =====================
#
# settings['operator'  ] = 'Rohde & Schwarz'
# settings['dut'       ] = 'DUT'
# settings['display'   ] = "default"
# settings['instrument']['connection type'         ] = 'socket'
# settings['instrument']['address'                 ] = '127.0.0.1'
# settings['save'      ]['disable global limit'    ]
# settings['save'      ]['disable touchstone files']
# settings['save'      ]['disable trace csv files' ]
# settings['save'      ]['disable screenshots'     ]
# settings['save'      ]['disable per-test limits' ]
# settings['save'      ]['disable markers'         ]
# settings['save'      ]['disable html summary'    ]
# settings['save'      ]['disable results json'    ]
# settings['save'      ]['organize by file'        ]
# settings['save'      ]['enable project csv'      ]

from collections    import defaultdict
from rstest.general import nand_keys, get_root_path

none_default_dict = defaultdict(lambda: None)

class Settings(defaultdict):
	def __init__(self, settings=None):
		super(Settings, self).__init__(lambda: None)
		if settings:
			self.update(settings)
		self['dut']        = self['dut'] or 'DUT'
		self['display']    = self['display'] or 'default'		
		self['instrument'] = self['instrument'] or none_default_dict.copy()
		instr = self['instrument']
		instr['connection type'] = instr['connection type'] or 'tcpip'
		instr['address']   = instr['address'] or '127.0.0.1'
		self['save']       = self['save'] or none_default_dict.copy()
		save  = self['save']
		save['directory']  = save['directory'] or str(get_root_path())

	def is_save_vna(self):
		keys = ['disable global limit', 'disable screenshots']
		return nand_keys(keys, self["save"])
	def is_save_channels(self):
		keys = ['disable touchstone files']
		return nand_keys(keys, self["save"])
	def is_save_diagrams(self):
		keys = ['disable screenshots', 'disable per-test limits']
		return nand_keys(keys, self["save"])
	def is_save_traces(self):
		keys = ['disable trace csv files', 'disable markers']
		return nand_keys(keys, self["save"])

	def copy(self):
		a_copy = Settings()
		a_copy.update(self)
		return a_copy

default = Settings()


