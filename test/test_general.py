import rstest.general
from   rohdeschwarz.instruments.vna import Vna
import unittest

class TestGeneral(unittest.TestCase):
    def setUp(self):
        vna = Vna()
        vna.open_tcp()
        vna.clear_status()
        vna.manual_sweep = True
        timeout_ms = 2*vna.sweep_time_ms + 5000
        vna.start_sweeps()
        vna.pause(timeout_ms)
        self.vna = vna

    def tearDown(self):
        self.vna.clear_status()
        self.vna.close()

    @classmethod
    def tearDownClass(self):
        vna = Vna()
        vna.open_tcp()
        vna.close()

    def test_get_ports(self):
        for i in self.vna.channels:
            ch = self.vna.channel(i)
            ports = rstest.general.get_ports(self.vna, ch)
            print("Ch{0} Ports: {1}".format(i, ports))
