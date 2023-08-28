"""
Given a string expression representing an expression of fraction addition and subtraction, 
return the calculation result in string format.
The final result should be an irreducible fraction. If your final result is an integer, 
change it to the format of a fraction that has a denominator 1. So in this case, 
2 should be converted to 2/1.

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
"""
import regex as re
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # split the expression into individual fractions
        fractions = re.findall('[+-]?\d+/\d+', expression)

        # convert the fractions into a list of tuples (numerator, denominator)
        fractions = [tuple(map(int, fraction.split('/'))) for fraction in fractions]

        # get the LCM (largest common multiple) of the denominators
        lcm = 1
        for fraction in fractions:
            lcm = lcm * fraction[1]

        # add the numerators after multiplying the appropriate factor
        numerator_sum = sum([fraction[0] * (lcm // fraction[1]) for fraction in fractions])

        # simplify the fraction
        gcd = math.gcd(numerator_sum, lcm)
        numerator = numerator_sum // gcd
        denominator = lcm // gcd

        return str(numerator) + "/" + str(denominator)


print(Solution.fractionAddition(Solution(), expression="-1/2+1/5-3/5"))