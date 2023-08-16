#!/usr/bin/python3


"""The function takes a list of int tuples as input, each tuple consists of a score and a weight. The function calculates the weighted average by multiplying each score with its corresponding weight and summing them up. It also keeps track of the total weight. Finally, it returns the weighted average by dividing the total score by the total weight.

If the input list is empty, the function returns 0 as specified in the requirements.the function has a default arg my_list=[], which means that if no argument is provided when calling the function, an empty list will be used as the default value."""


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    
    total_score = 0
    total_weight = 0
    
    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight
    
    return total_score / total_weight
