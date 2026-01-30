"""
Test file for the calculate_pi function in main.py
"""
import unittest
from main import calculate_pi


class TestCalculatePi(unittest.TestCase):
    """Test cases for the calculate_pi function"""
    
    def test_pi_5_digits(self):
        """Test pi calculation to 5 decimal places"""
        result = calculate_pi(5)
        expected = 3.14159
        self.assertEqual(result, expected, 
                        f"Expected {expected}, but got {result}")
    
    def test_pi_3_digits(self):
        """Test pi calculation to 3 decimal places"""
        result = calculate_pi(3)
        expected = 3.142
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_1_digit(self):
        """Test pi calculation to 1 decimal place"""
        result = calculate_pi(1)
        expected = 3.1
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_pi_10_digits(self):
        """Test pi calculation to 10 decimal places"""
        result = calculate_pi(10)
        expected = 3.1415926536
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
    
    def test_return_type(self):
        """Test that the function returns a float"""
        result = calculate_pi(5)
        self.assertIsInstance(result, float,
                            f"Expected float type, but got {type(result)}")
    
    def test_pi_default_parameter(self):
        """Test that default parameter is 5 digits"""
        result = calculate_pi()
        expected = 3.14159
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")


def run_manual_tests():
    """Run some manual tests and print results"""
    print("Manual Testing of calculate_pi function")
    print("=" * 50)
    
    test_cases = [1, 2, 3, 5, 10]
    expected_values = {
        1: 3.1,
        2: 3.14,
        3: 3.142,
        5: 3.14159,
        10: 3.1415926536
    }
    
    for digits in test_cases:
        result = calculate_pi(digits)
        expected = expected_values.get(digits, "Unknown")
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} | Pi to {digits:2d} digits: {result} (expected: {expected})")
    
    print("=" * 50)
    print("\nActual value of pi for reference: 3.14159265358979323846...")


if __name__ == "__main__":
    # Run manual tests first
    run_manual_tests()
    
    # Run unit tests
    print("\nRunning Unit Tests:")
    print("=" * 50)
    unittest.main(verbosity=2)
