'''Test for merge_sort() function'''
from hw2_debugging import merge_sort

a1 = [9, 8, 7, 6, 5, 4, 3, 2, 0]
a2 = [-9, -2, -3, -1, -10, -11]
a3 = [1, 2, 3, 4, 5, 6, 0, 10]


def test1_merge_sort():
    '''Test merge sort with all elements in descending order'''
    b1 = sorted(a1)
    assert merge_sort(a1) == b1


def test2_merge_sort():
    '''Test merge sort with negative elments'''
    b2 = sorted(a2)
    assert merge_sort(a2) == b2


def test3_merge_sort():
    '''Test merge sort with elements in random order'''
    b3 = sorted(a3)
    assert merge_sort(a3) == b3
