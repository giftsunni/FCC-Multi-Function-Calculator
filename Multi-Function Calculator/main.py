from sympy import symbols, Eq, solve, sqrt, simplify
from fractions import Fraction

def solve_proportion(a, b, c=None, d=None):
    # Solve proportions a/b = c/d
    x = symbols('x')
    if c is None:
        equation = Eq(a/b, x/d)
    elif d is None:
        equation = Eq(a/b, c/x)
    else:
        return "Provide one unknown (c or d) as None."
    return solve(equation, x)[0]

def solve_for_x(equation):
    # Solve for x in ax + b = c
    x = symbols('x')
    eq = Eq(eval(equation.split('=')[0]), eval(equation.split('=')[1]))
    return solve(eq, x)

def factor_square_root(number):
    return simplify(sqrt(number))

def decimal_to_fraction_and_percent(decimal):
    fraction = Fraction(decimal).limit_denominator()
    percent = decimal * 100
    return fraction, f"{percent}%"

def fraction_to_decimal_and_percent(numerator, denominator):
    decimal = numerator / denominator
    percent = decimal * 100
    return decimal, f"{percent}%"

def percent_to_decimal_and_fraction(percent):
    decimal = percent / 100
    fraction = Fraction(decimal).limit_denominator()
    return decimal, fraction

# Example Usage
print("Solve Proportion: ", solve_proportion(3, 4, d=8))
print("Solve for x: ", solve_for_x("2*x + 5 = 15"))
print("Factor Square Root: ", factor_square_root(50))
print("Decimal to Fraction and Percent: ", decimal_to_fraction_and_percent(0.75))
print("Fraction to Decimal and Percent: ", fraction_to_decimal_and_percent(3, 4))
print("Percent to Decimal and Fraction: ", percent_to_decimal_and_fraction(75))