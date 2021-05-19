from pytest import approx

def add(a,b):
    return a + b

def test_add():
    assert add(2,3) == 5
    assert add('space', 'ship') == 'spaceship'
    assert add(0.1,0.2) == approx(0.3)

def subtract(a,b):
    return a - b

def test_subtract():
    assert subtract(5,2) == 3
    assert subtract(0.9,0.5) == approx(0.4)

