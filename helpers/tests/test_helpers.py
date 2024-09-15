# tests/test_helpers.py
from helpers.generate_linear import generate_equation

def test_generate_equation_contains_x():
    equation, res = generate_equation()
    assert "x" in equation

def test_solution_is_integer():
    _, solution = generate_equation()
    assert isinstance(solution, int)

def test_equation_is_correct():
    equation, solution = generate_equation()
    coefficient, result = map(int, equation.replace('x = ', ' ').split())
    assert coefficient * solution == result

def test_largest_number_is_less_than_20():
    equation, solution = generate_equation()
    coefficient, result = map(int, equation.replace('x = ', ' ').split())
    assert max(coefficient, result, solution) < 20
