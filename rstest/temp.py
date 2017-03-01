from rstest.general import get_root_path
from collections    import defaultdict

none_default_dict = defaultdict(lambda: None)

instrument = none_default_dict.copy()
instrument['connection type'] = 'socket'
instrument['address']         = '127.0.0.1'

save = none_default_dict.copy()
save['directory'] = str(get_root_path())
# save['disable global limit']     = True
# save['disable touchstone files'] = True
# save['disable trace csv files']  = True
# save['disable screenshots']      = True
# save['disable per-test limits']  = True
# save['disable markers']          = True
# save['disable html summary']     = True
# save['disable results json']     = True
# save['organize by file']         = True
# save['enable project csv']       = True

settings = none_default_dict.copy()
settings['operator']   = 'Rohde & Schwarz'
settings['dut']        = 'DUT'
settings['display']    = "default"
settings['instrument'] = instrument
settings['save']       = save
