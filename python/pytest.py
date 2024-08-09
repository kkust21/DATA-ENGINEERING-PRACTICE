import pytest

def capital_case(x):
    if not isinstance(x,str):
        raise TypeError("Please provide a string argument")
    return x.capitalize()

def isEven(num):
    if not isinstance(num,int):
        raise TypeError("Please provide a integer argument")
    return num%2



def test_isEven():
    assert isEven(20) == 0 # assert checks the condition



