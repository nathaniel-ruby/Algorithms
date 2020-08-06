""""
Reverse Stack Algorithm
                                        
Write function uses 'Stack' to 
reverse characters in a string
                                        
Author: Nathaniel Ruby                  
Date: 08/06/2020                        
"""

import sys
sys.path.append("/Users/nathaniel.ruby/Dropbox/Search/Import/")

from module_class import Stack

def string_create(length):
    letters      = string.ascii_lowercase
    final_string = ''.join(random.choice(letters) for i in range(length))
    return final_string

def string_reverse(chars):
    fwd_string = string_create(chars) 
    print(fwd_string)
    int_stack = Stack()
    for str in fwd_string:
        int_stack.push(str)
    rev_string = ""
    while not int_stack.isEmpty():
        rev_string += int_stack.pop()

    return rev_string 
    
    
