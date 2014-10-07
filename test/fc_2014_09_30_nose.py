from fc_2014_09_30 import Borg, SubBorg

def test_borg():
    a = Borg()
    b = Borg()
    a.a = 'hi'
    assert b.a == 'hi'

def test_subborg():
    a = Borg()
    b = SubBorg()
    a.a = 'HI'
    b.b = 'AWESOME'
    assert b.a == 'HI'
    assert a.b == 'AWESOME'
