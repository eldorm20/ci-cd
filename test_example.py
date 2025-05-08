# Function to test
def add(x, y):
    return x + y

# Test cases
def test_add():
    assert add(2, 3) == 5  # ✅ Correct test

def test_negative_numbers():
    assert add(-2, -3) == -5  # ✅ Correct test

def test_zero():
    assert add(0, 0) == 0  # ✅ Correct test

# Intentional failing test
def test_failure():
    assert add(2, 2) == 5  # ❌ Wrong expected result!
