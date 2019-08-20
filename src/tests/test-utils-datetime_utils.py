import unittest
import sys

sys.path.append("..")
from utils import datetime_utils


class TestDatetimeUtils(unittest.TestCase):
    """
    Will run unittests for the /src/utils/datetime_utils.py
    """

    def test_cast_regular_as_datetime(self):
        """
        Tests the cast_regular_as_datetime function
        """
        result = datetime_utils.cast_regular_as_datetime(
            "2019-08-19 05:51:45.694869")
        self.assertEqual(result.year, 2019)
        self.assertEqual(result.month, 8)
        self.assertEqual(result.day, 19)
        self.assertEqual(result.hour, 5)
        self.assertEqual(result.minute, 51)
        self.assertEqual(result.second, 45)


if __name__ == '__main__':
    unittest.main()
