def greeting():
    print("Hi There!")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of digits after the decimal point.
    Uses the Machin formula for efficient and accurate calculation:
    pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        digits: Number of decimal places to calculate (default: 5)
    
    Returns:
        float: Pi calculated to the specified precision
    """
    from decimal import Decimal, getcontext
    
    # Set precision higher than needed for accurate rounding
    getcontext().prec = digits + 10
    
    def arctan(x, num_terms=100):
        """Calculate arctan using Taylor series expansion"""
        x = Decimal(x)
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(Decimal(1)/Decimal(5), 100) - arctan(Decimal(1)/Decimal(239), 100))
    
    # Round to the specified number of digits
    return round(float(pi), digits)