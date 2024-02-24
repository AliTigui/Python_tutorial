from main import square

# Approche 1
def test_square():
    assert square(1)==1
    assert square(2)==4
    assert square(3)==9
    assert square(4)==16
# Approche 2  
def test_square():
    try:
        assert square(1)==1
    except AssertionError:
        print("square 1 was not 1")
    try:
        assert square(2)==4
    except AssertionError:
        print("square 2 was not 4")
    try:
        assert square(3)==9
    except AssertionError:
        print("square 3 was not 9")
    try:
        assert square(4)==16
    except AssertionError:
        print("square 4 was not 16")
test_square()
