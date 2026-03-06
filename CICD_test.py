import pytest
def add(a,b):
    return a+b
def multy(a,b):
    return a*b

def test_evaluvationadd():
    assert add(5,5) == 10

def test_evaluvationmulty():
    assert multy(5,5) == 25
