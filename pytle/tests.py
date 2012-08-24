from pytle.parser import TLEParameters
import unittest

class TLEParametersTest(unittest.TestCase):

    def setUp(self):
        #TLE taken from http://en.wikipedia.org/wiki/Two-line_element_set
        three_line = '''ISS (ZARYA)
        1 25544U 98067A   08264.51782528 -.00002182  00000-0 -11606-4 0  2927
        2 25544  51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537'''

        self.tle_parameters = TLEParameters(tle_string=three_line)

    def test_name(self):
        self.assertEquals('ISS (ZARYA)',self.tle_parameters.name)

    def test_international_designator(self):
        self.assertEquals('98067A',self.tle_parameters.international_designator)

    def test_satellite_number(self):
        self.assertEquals(25544,self.tle_parameters.satellite_number)

    def test_mean_motion_dot(self):
        self.assertEquals(-0.00002182*2,self.tle_parameters.mean_motion_dot)

    def test_mean_motion_ddot(self):
        self.assertEquals(0,self.tle_parameters.mean_motion_ddot)

    def test_bstar(self):
        self.assertEquals(-0.11606,self.tle_parameters.bstar)

    def test_epoch_day(self):
        self.assertEquals(264.51782528,self.tle_parameters.epoch_day)

    def test_epoch_year(self):
        self.assertEquals(2008,self.tle_parameters.epoch_year)

    def test_classification(self):
        self.assertEquals('U',self.tle_parameters.classification)

    def test_element_number(self):
        self.assertEquals(292,self.tle_parameters.element_number)

    def test_inclination(self):
        self.assertEquals(51.6416,self.tle_parameters.inclination)

    def test_ra_of_asc_node(self):
        self.assertEquals(247.4627,self.tle_parameters.ra_of_asc_node)

    def test_eccentricity(self):
        self.assertEquals(.0006703,self.tle_parameters.eccentricity)

    def test_arg_of_perigee(self):
        self.assertEquals(130.5360,self.tle_parameters.arg_of_perigee)

    def test_mean_anomaly(self):
        self.assertEquals(325.0288,self.tle_parameters.mean_anomaly)

    def test_mean_motion(self):
        self.assertEquals(15.72125391,self.tle_parameters.mean_motion)

    def test_rev_at_epoch(self):
        self.assertEquals(56353,self.tle_parameters.rev_at_epoch)

    def test_json(self):
        expected = '{"international_designator": "98067A", "mean_motion_ddot": 0.0, "mean_motion": 15.72125391, "ra_of_asc_node": 247.4627, "name": "ISS (ZARYA)", "classification": "U", "rev_at_epoch": 56353, "bstar": -0.11606, "satellite_number": 25544, "element_number": 292, "epoch_day": 264.51782528, "arg_of_perigee": 130.536, "mean_anomaly": 325.0288, "mean_motion_dot": -4.364e-05, "eccentricity": 0.0006703, "epoch_year": 2008, "inclination": 51.6416}'

        self.assertEquals(expected,self.tle_parameters.json)

if __name__ == '__main__':
    unittest.main()
