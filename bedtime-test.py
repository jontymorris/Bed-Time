import unittest, datetime

# debug code for import
import os, sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import bedtime


class TestIsBedtime(unittest.TestCase):

    def test_sunday(self):
        time = datetime.datetime(2018, 1, 7, hour=21, minute=20)
        self.assertFalse( bedtime.is_bedtime(time), "Sunday 9:20pm is not bed time" )
        
        time = datetime.datetime(2018, 1, 7, hour=21, minute=30)
        self.assertTrue( bedtime.is_bedtime(time), "Sunday 9:30pm is bed time" )
    
    def test_friday(self):
        time = datetime.datetime(2018, 1, 5, hour=22)
        self.assertFalse( bedtime.is_bedtime(time), "Friday 10pm is not bed time" )

        time = datetime.datetime(2018, 1, 5, hour=23)
        self.assertTrue( bedtime.is_bedtime(time), "Friday 11pm is bed time" )


if __name__ == "__main__":
    unittest.main()