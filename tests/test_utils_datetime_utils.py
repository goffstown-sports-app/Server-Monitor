from utils import datetime_utils


def test_cast_regular_as_datetime():
    """
    Tests the cast_regular_as_datetime function
    """
    result = datetime_utils.cast_regular_as_datetime(
        "2019-08-19 05:51:45.694869")
    assert result.year == 2019
    assert result.month == 8
    assert result.day == 19
    assert result.hour == 5
    assert result.minute == 51
    assert result.second == 45
