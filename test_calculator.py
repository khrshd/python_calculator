from calculator import add, subtract
#python's testing method
import pytest
def test__add():
    test1 = add(1, 3)
    #we knbow 4 is the right answer, but also program has to know that it is 4:
    assert(test1 == 4)

    test2 = add(5.0, 5.0)
    assert(test2 == 10.0)

def test__subtract():
    test3 = subtract(4, 1)
    assert(test3 == 3)

    test4 = subtract(2.5, 6.8)
    assert(test4 == -4.3)
