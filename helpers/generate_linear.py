import random

def generate_equation():
    """
    Generates a linear equation of the form coefficient * x = result, where
    the coefficient and result are whole numbers, and returns both the equation
    as a string and the solution.
    
    Returns:
        tuple: A tuple containing the equation as a string and the solution as an integer.
    """
    solution = random.randint(1, 10)
    coefficient = random.randint(1, 10)
    result = coefficient * solution
    equation = f"{coefficient}x = {result}"
    
    return equation, solution
