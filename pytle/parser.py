import json

def parse(filename=None,tle_string=None):
    if filename:
        f = open(filename)
        tle_string = f.read()
        f.close()
    else:
        pass

    if tle_string:
        line_list = tle_string.split('\n')

class TLEParameters(object):

    def __init__(self,tle_string=None,name=None,line1=None,line2=None):
        """

        """
        if tle_string:
            tle_lines = tle_string.split('\n')
            if len(tle_lines) == 2:
                self.line1 = tle_lines[0].strip()
                self.line2 = tle_lines[1].strip()
            elif len(tle_lines) == 3:
                self._name = tle_lines[0].strip()
                self.line1 = tle_lines[1].strip()
                self.line2 = tle_lines[2].strip()
            else:
                pass
        else:
            if line1 and line2:
                self.line1 = line1.strip()
                self.line2 = line2.strip()

                if name:
                    self._name = name

        if self.line1:
            if len(self.line1) != 69:
                pass

        if self.line2:
            if len(self.line2) !=69:
                pass

    def parse_tle_number(self,tle_number_string):
        """

        """
        split_string = tle_number_string.split('-')
        if len(split_string)==3:
            new_number = '-'+ str(split_string[1]) + 'e-' + str(int(split_string[2])+1)
        elif len(split_string)==2:
            new_number = str(split_string[0]) + 'e-' + str(int(split_string[1])+1)
        elif len(split_string)==1:
            new_number = '0.' + str(split_string[0])
        else:
            raise TypeError('Input is not in the TLE float format')

        return float(new_number)

    @property
    def name(self):
        """

        """
        if self._name:
            return self._name
        else:
            return None

    @property
    def international_designator(self):
        """

        """
        if self.line1:
            return self.line1[9:17].strip()
        else:
            return None

    @property
    def classification(self):
        """

        """
        if self.line1:
            return self.line1[7:8]
        else:
            return None

    @property
    def mean_motion_dot(self):
        """

        """
        if self.line1:
            return float(self.line1[33:43])*2
        else:
            return None

    @property
    def mean_motion_ddot(self):
        """

        """
        if self.line1:
            return self.parse_tle_number(self.line1[44:52])*6.0
        else:
            return None

    @property
    def bstar(self):
        """

        """
        if self.line1:
            return self.parse_tle_number(self.line1[53:61])
        else:
            return None

    @property
    def element_number(self):
        """

        """
        if self.line1:
            return int(self.line1[64:68].strip())
        else:
            return None

    @property
    def satellite_number(self):
        """

        """
        if self.line1:
            return int(self.line1[2:7].strip())
        else:
            return None

    @property
    def inclination(self):
        """

        """
        if self.line2:
            return float(self.line2[8:16].strip())
        else:
            return None

    @property
    def ra_of_asc_node(self):
        """

        """
        if self.line2:
            return float(self.line2[17:25].strip())
        else:
            return None

    @property
    def arg_of_perigee(self):
        """

        """
        if self.line2:
            return float(self.line2[34:42].strip())
        else:
            return None

    @property
    def mean_anomaly(self):
        """

        """
        if self.line2:
            return float(self.line2[43:51])
        else:
            return None

    @property
    def eccentricity(self):
        """

        """
        if self.line2:
            return self.parse_tle_number(self.line2[26:33].strip())
        else:
            return None

    @property
    def rev_at_epoch(self):
        """

        """
        if self.line2:
            return int(self.line2[63:68])
        else:
            return None

    @property
    def two_digit_year(self):
        """

        """
        if self.line1:
            return int(self.line1[18:20])
        else:
            return None

    @property
    def epoch_year(self):
        """

        """
        if self.line1:
            two_digit_year = self.two_digit_year
            if self.two_digit_year > 56:
                return two_digit_year+1900
            else:
                return two_digit_year+2000

    @property
    def epoch_day(self):
        """

        """
        if self.line1:
            return float(self.line1[20:32])
        else:
            return None

    @property
    def mean_motion(self):
        if self.line2:
            return float(self.line2[52:63])
        else:
            return None

    @property
    def json(self):
        dict_value = {
            'name':self.name,
            'international_designator':self.international_designator,
            'classification':self.classification,
            'mean_motion_dot':self.mean_motion_dot,
            'mean_motion_ddot':self.mean_motion_ddot,
            'bstar':self.bstar,
            'element_number':self.element_number,
            'satellite_number':self.satellite_number,
            'inclination':self.inclination,
            'ra_of_asc_node':self.ra_of_asc_node,
            'arg_of_perigee':self.arg_of_perigee,
            'mean_anomaly':self.mean_anomaly,
            'eccentricity':self.eccentricity,
            'rev_at_epoch':self.rev_at_epoch,
            'epoch_year':self.epoch_year,
            'epoch_day':self.epoch_day,
            'mean_motion':self.mean_motion
        }

        return json.dumps(dict_value)



