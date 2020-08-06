""""
Hot Potato Algorithm
                                        
Write function uses 'Queue' to 
play Hot Potato
                                        
Author: Nathaniel Ruby                  
Date: 08/06/2020                        
"""

import sys
sys.path.append("/Users/nathaniel.ruby/Dropbox/Search/Import/")

from module_class import Queue 

def random_rounds():
    time = random.randint(0,60)
    return time

def hotPotato(namelist):
    circle = Queue()
    for name in namelist:
        circle.enqueue(name)
    seconds = random_rounds()
    while circle.size() > 1: 
        for count in range(seconds):
            circle.enqueue(circle.dequeue())
        seconds = random_rounds() 
        circle.dequeue()
    return circle.dequeue()

hotPotato_winner = hotPotato(["Molly","Sasha","Karen","Ned"])


    
    
