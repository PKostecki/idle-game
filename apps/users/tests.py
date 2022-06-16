from django.test import TestCase


def inc(x):
    return x + 1


def test_test():
    assert inc(3) == 4


def test_2():
    assert 2 == 2


def test_3():
    assert 2 == 3


