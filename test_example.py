# Function to test
def add(x, y):
    return x + y

# Test cases
def test_add():
    assert add(2, 3) == 5

def test_negative_numbers():
    assert add(-2, -3) == -5

def test_zero():
    assert add(0, 0) == 0
