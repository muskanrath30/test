from mytest import square

import pytest

@pytest.fixture
def input_value():
    return 4

#def test_square_gives_correct_value():
#    subject=square(2)   # we are calling the function square to find square of 2, in other words if we enter 2 it should give 4 in result
#    assert subject==4  # if the square of 2 is equal to 4, test will pass otherwise it will fail

def test_square_gives_correct_value(input_value):
    subject = square(4)
    assert subject == 16


# pytest comes with an assert statement which gives details on test passing or failing
# fixtures treated as input to other functions
# parameterising variable - we can use across the whole code
# after writing this code, save this code, open the terminal and run the following commands
# pip install pytest
# pytest

# Refer: pytest fixture
# pytest : predefined classes,output objects we can use, input function we can use as a parameter in any of the test f