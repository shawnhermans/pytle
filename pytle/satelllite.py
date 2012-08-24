from math import pi, floor

xj3 = -2.53881E-6
ck2 = 5.41308E-4
ck4 = 6.2098875E-7
xke = 0.0743669161331734132    # = (G*M)^(1/2)*(er/min)^(3/2) where G =Newton's grav const, M = earth mass
xkmper = 6378.135 # equatorial earth radius, km

#/* SGP4 density constants.  qoms2t = ((qo - so) / xkmper) ** 4,
#s = 1 + so / xkmper, where qo = 120 and so = 78 */

qoms2t = 1.880279159015270643865e-9
a3ovk2 = -1.*xj3/ck2
s = 1.0122292801892716

def julian_date_of_year(the_year):
    """
	 * Calculates the Julian Day of the Year.
	 *
	 * The function Julian_Date_of_Year calculates the Julian Date
	 * of Day 0.0 of {year}. This function is used to calculate the
	 * Julian Date of any date by using Julian_Date_of_Year, DOY,
	 * and Fraction_of_Day.
	 *
	 * Astronomical Formulae for Calculators, Jean Meeus,
	 * pages 23-25. Calculate Julian Date of 0.0 Jan aYear
	 *
	 * @param theYear the year
	 * @return the Julian day number
    """
    a_year = theYear - 1
    i = floor(a_year / 100)
    a = i

    i = a / 4
    b = 2 - a + i
    i = floor(365.25 * a_year)
    i += 30.6001 * 14
    result = i + 1720994.5 + b

    return result