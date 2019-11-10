
"""
Verifying Ramanujan's Theorem

Author: Oğuzhan Çölkesen
"""

from math import sqrt

def verify_ramanujan_theorem():
    """
    Verifies the validity of one of Ramanujan's theorems involving radicals.
    """
    four_root_five = sqrt(sqrt(5))
    four_root_hundred_twenty_five = sqrt(sqrt(125))
    print("The value of the left-hand side of Ramanujan's theorem:")
    print((four_root_five + 1) / (four_root_five - 1))
    print("The value of the right-hand side of Ramanujan's theorem:")
    print(0.5 * (3 + four_root_five + sqrt(5) + four_root_hundred_twenty_five))