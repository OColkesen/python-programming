
"""
Computing the time it takes to do laundry

Author: Oğuzhan Çölkesen
"""

def compute_laundry_time():
    """
    Computes and prints out the minimum number of minutes required to
    do a user-specified number of loads of laundry.

    Assumptions: There is only 1 washer and 1 dryer. Washing takes 25 minutes,
    drying takes 25 minutes, and folding takes 10 minutes.
    """
    num_loads = int(input("Enter the number of loads: "))
    laundry_time = 60
    
    for i in range (1,num_loads):
        laundry_time = laundry_time + 25

    print(laundry_time)