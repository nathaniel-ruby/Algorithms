""""
Hill Climbing Algorithms                
                                        
Write a function that                   
generates one sentence of Shakespeare   
                                        
Author: Nathaniel Ruby                  
Date: 06/09/2020                        
"""

import random 
import string

abcd = string.ascii_lowercase + " "

"""
Generates string 
n characters long
"""
def docstring(updatetest, checkmatch):
    list_updatetest = list(updatetest)
    for i in range(len(updatetest)):
        if (checkmatch[i] == 0):
            list_updatetest[i] = random.choice(abcd) 
    return ''.join(list_updatetest) 
    
def updatematch(goal, test, match):
    updatedtest = docstring(test, match)
    for i in range(len(goal)):
        if (goal[i] == updatedtest[i]):
            match[i] = 1            
    return (updatedtest, match)

def countmatch():
    goal_string     = "methinks it is like a weasel"
    test_string     = "".join(random.choice(abcd) for i in range(len(goal_string)))
    match_correct   = [0 for i in range(len(goal_string))]
    num_correct     = sum(match_correct)
    count           = 0
    while num_correct < len(goal_string):
        test_string, match_correct = updatematch(goal_string, test_string, match_correct)
        num_correct = sum(match_correct)
        count       = count+1
        "This is num correct "+str(num_correct)

    return (count, test_string, match_correct)

