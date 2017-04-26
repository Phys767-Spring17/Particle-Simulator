from quark import Quark
import pytest

t = Quark()

def test_quark_1():
    t.flavor = "up"
    t.flip()
    assert t.flavor == "down"

def test_quark_2():
    t.flavor = "down"
    t.flip()
    assert t.flavor == "up"

def test_quark_3():
    t.flavor = "top"
    t.flip()
    assert t.flavor == "bottom"

def test_quark_4():
    t.flavor = "bottom"
    t.flip()
    assert t.flavor == "top"

def test_quark_5():
    t.flavor = "strange"
    t.flip()
    assert t.flavor == "charm"

def test_quark_6():
    t.flavor = "charm"
    t.flip()
    assert t.flavor == "strange"
