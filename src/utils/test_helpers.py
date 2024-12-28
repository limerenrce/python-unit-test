# Helper methods for testing purposes.


def generate_random_array(size, min_val, max_val):
    """Generates an array of random integers for testing."""
    import random

    return [random.randint(min_val, max_val) for _ in range(size)]
