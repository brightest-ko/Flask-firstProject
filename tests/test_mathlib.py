import mathlib
import pytest
import sys

#@pytest.mark.skip(reason="I dont want to run this test at the moment")
@pytest.mark.skipif(sys.version_info > (2,5) , reason="I dont want to run this test at the moment")
def test_calc_total():
    result = mathlib.calc_total(4,5)
    assert result == 7
    
    
def test_cal_multiply():
    result = mathlib.cal_multiply(2,5)
    assert result == 10

#**test is prefix, if non test_ is no test    
#python -m pytest
#py.test
#py.test -v
#py.test -v -rxs , it can watch reason
