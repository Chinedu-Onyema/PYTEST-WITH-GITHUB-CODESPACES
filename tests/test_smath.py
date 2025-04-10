from smath import subtract

# Setup function
def setup_function(function):
    print(f"Running Setup: {function.__name__}")
    function.x = 10

# Teardown function
def teardown_function(function):
    print(f"Running Teardown: {function.__name__}")
    del function.x  # Proper way to delete the attribute

# Test function
def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
