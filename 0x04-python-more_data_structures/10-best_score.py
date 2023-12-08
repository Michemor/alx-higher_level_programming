#!/usr/bin/python3
def best_score(a_dictionary):
    """
    checks among the keys of a dictionary which contains the highest value
    """
    if not a_dictionary:
        return None
    max_val = 0
    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            max_key = k
    return max_key
