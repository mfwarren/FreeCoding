from fc_2014_10_04 import nth_fib, sum, product

def test_sum_2_3():
    assert sum(2,3) == 5

def test_product_2_3():
    assert product(2,3) == 6

def test_first_10_fib():
    assert nth_fib(0) == 0
    assert nth_fib(1) == 1
    assert nth_fib(2) == 1
    assert nth_fib(3) == 2
    assert nth_fib(4) == 3
    assert nth_fib(5) == 5
    assert nth_fib(6) == 8
    assert nth_fib(7) == 13
    assert nth_fib(8) == 21
    assert nth_fib(9) == 34
