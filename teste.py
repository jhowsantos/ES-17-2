import pytest
from principal import somar
from principal import sub
from principal import multi
from principal import div

def test_somar():
    assert somar(2,3)==5

def test_sub():
    assert sub(5,2)==3

def test_multiplicar():
    assert multi(2,3)==6

def test_dividir():
    assert div(10,2)==5 # teste