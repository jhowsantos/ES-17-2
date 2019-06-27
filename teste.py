import pytest
from principal import somar
from principal import sub

def test_somar():
    assert somar(2,3)==5

def test_sub():
    assert sub(5,2)==3