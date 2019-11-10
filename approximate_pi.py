
"""
Approximating pi

Author: Oğuzhan Çölkesen
"""

def approximate_pi():
    """
    Computes an approximation to pi using the Leibniz formula.
    """
    num_terms = int(input("How many terms would you like to use? "))
    addition_coefficient = 0
    subtraction_coefficient = 0
    
    for i in range (num_terms // 2):
        addition_coefficient += 1/(1+(4*i))
        subtraction_coefficient += 1/(3+(4*i))
        
    pi_approximation = 4 * (addition_coefficient - subtraction_coefficient)
    print (pi_approximation)