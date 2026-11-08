import pytest

def test_m1():
    a=3
    b=4
    assert a+1 == b, "Test Failed"
    assert a==b, "Test Failed as a not equal to b"

def test_m2():
    a = "selenium"
    assert a.upper == "SELENIUM"

def test_m3():
    assert True

def test_m4():
    assert False

def test_login():
    assert 'admin' == 'admin'