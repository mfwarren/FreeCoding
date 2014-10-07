from fc_2014_10_05 import find_files

def test_find_files():
    #find this file
    assert find_files('.', 'fc_2014_10_05_*.py').next().endswith('fc_2014_10_05_nose.py')
