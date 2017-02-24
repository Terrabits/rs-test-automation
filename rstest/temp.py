from rstest.general import get_root_path

instrument = {}
instrument['connection type'] = 'socket'
instrument['address']         = '127.0.0.1'

save = {}
save['directory'] = str(get_root_path())
save['disable touchstone files'] = False
save['disable trace csv files']  = False
save['disable screenshots']      = False
save['disable html summary']     = False
save['disable results json']     = False
save['organize by file']         = True

settings = {}
settings['operator']   = 'Rohde & Schwarz'
settings['dut']        = 'DUT'
settings['display']    = "default"
settings['instrument'] = instrument
settings['save']       = save
