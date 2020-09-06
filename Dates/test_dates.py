
import unittest

import Dates.dates as dates

class TestDates(unittest.TestCase):

    def test_001_leap_year_1977(self):
        self.assertFalse(dates.leap_year(1977))

    def test_002_leap_year_2000(self):
        self.assertTrue(dates.leap_year(2000))

    def test_003_leap_year_1900(self):
        self.assertFalse(dates.leap_year(1900))

    def test_010_days_per_year_1977(self):
        self.assertEqual(365, dates.days_per_year(1977))

    def test_011_days_per_year_2000(self):
        self.assertEqual(366, dates.days_per_year(2000))

    def test_020_days_between_years(self):

        print( dates.days_between_years(2000,2001) )
        print( dates.days_between_years(2000,2002) )

    def test_030_days_in_month(self):
        self.assertEqual( 31, dates.days_in_month(2000, 1))
        self.assertEqual( 31, dates.days_in_month(2000, 3))
        self.assertEqual( 30, dates.days_in_month(2000, 4))
        self.assertEqual( 29, dates.days_in_month(2000, 2))
        self.assertEqual( 28, dates.days_in_month(2001, 2))

    def test_040_add_one_day(self):

        self.assertEqual( (2019, 4, 6), dates.add_one_day( (2019, 4, 5 )) )
        self.assertEqual( (2019, 1, 2), dates.add_one_day( (2019, 1, 1 )) )
        self.assertEqual((2019, 2, 1), dates.add_one_day((2019, 1, 31)))
        self.assertEqual((2019, 2, 21), dates.add_one_day((2019, 2, 20)))
        self.assertEqual((2019, 2, 28), dates.add_one_day((2019, 2, 27)))
        self.assertEqual((2019, 3, 1), dates.add_one_day((2019, 2, 28)))
        self.assertEqual((2000, 2, 29), dates.add_one_day((2000, 2, 28)))
        self.assertEqual((2001, 1, 1), dates.add_one_day((2000, 12, 31)))

    def test_050_days_between_dates(self):

        self.assertEqual( 5, dates.days_between_dates( (2019, 5, 5), ( 2019, 5, 10) ))
        self.assertEqual( 5843, dates.days_between_dates( (2000, 1, 1), ( 2015, 12, 31) ))