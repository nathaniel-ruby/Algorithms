""""
Anagram Algorithm
                                        
Write function that determines
if two strings are anagrams 
                                        
Author: Nathaniel Ruby                  
Date: 08/04/2020                        
"""

import random
import string

def string_create(length):
    letters      = string.ascii_lowercase
    final_string = ''.join(random.choice(letters) for i in range(length))
    return final_string

def anagramfinder(chars):
    pos1 = [0]*26
    pos2 = [0]*26

    string1 = string_create(chars)
    print(string1)
    string2 = string_create(chars)
    print(string2)
    
    for i in range(len(string1)):
        alph = ord(string1[i]) - ord("a")
        pos1[alph] = pos1[alph]+1

    for i in range(len(string2)):
        alph = ord(string2[i]) - ord("a")
        pos2[alph] = pos2[alph]+1

    anagram = True
    j = 0 
    while j<26 and anagram:
        if pos1[j] == pos2[j]:
            j = j+1
        else:
            anagram = False
    return anagram

print(anagramfinder(10))
            
        
