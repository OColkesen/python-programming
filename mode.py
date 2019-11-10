
"""
Finding the mode in a list

Author: Oğuzhan Çölkesen
"""

def compute_mode(scores):
    """ Returns the mode(s) of the supplied data.

    In case the mode is not unique, then the list of modes returned is in
    ascending order.

    Parameters:
        scores - a list of integers denoting the data whose mode we wish to
                 compute.

    Returns:
        A list of integers denoting the mode(s) of the data (sorted in
        ascending order).
    """
    scores_dictionary = {}
    
    for i in scores:
        if i in scores_dictionary:
            scores_dictionary[i] += 1
        else:
            scores_dictionary[i] = 1
    
    maximum_occurance = 0
    
    for i in scores_dictionary:
        maximum_occurance = max(maximum_occurance, scores_dictionary[i])
        
    modes = []
    
    for i in scores:
        if (scores_dictionary[i] == maximum_occurance and i not in modes):
            modes.append(i)
    
    modes.sort()
    
    return modes

def main():
    """ Tester function """
    print("Testing compute_mode")
    print(compute_mode([65, 70, 88, 70]))
    print(compute_mode([88, 70, 65, 70, 88]))
    print(compute_mode([92, 56, 14, 73, 22, 38, 93, 45, 55]))

if __name__ == "__main__":
    main()