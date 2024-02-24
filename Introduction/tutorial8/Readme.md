## Tutorial 7
This tutorial will see unit testing in python 

### testing using assert 
one of basic formate of tessting our code is using the `assert` keyword this keyword will raise Asserterror if the result of assertation is not True  
with this approch we just create module for testing and we iport function that we test to it and then we use multiple assertation, we can also use multiple try except blocks so we can catch the Assert errors and and print discrptive taxt for each error
#### Example 
```Python
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
```
### testing using pytest
as we see we can make our test with the assertation methodes but this approch have problem ,the more we want to make test the longer our testing code get ,so we can end up writing large block of code just to test simple functions  
better way to make test is using 3 party library and one of the best and simplest one is pytest, using pytest is same we just write function for testing and then instead of using python to run our code we use pytest  
we can also devide the testing into many test function with this we can test different scenarios and know what will cuz our programe to crash and what not  
we can also write test for errors and check if our programe will rise them or no
#### Example
```Python
from main import square
import pytest

def test_negative():
    assert square(-4) == 16
    assert square(-2) == 4
    assert square(-3) == 9
def test_positive():
    assert square(4) == 16
    assert square(2) == 4
    assert square(3) == 9
def test_zero():
    assert square(0) == 0
def test_error():
    with pytest.raises(TypeError):
        square("cat")
```
### testing multiple file
we can create folder as package called test  and put inside it all test we want to do ,then run pytest and pass the folder name to is so pytest will test all files inside that folder  
to tell python that a specific folder is package we should add __init__.py to it 