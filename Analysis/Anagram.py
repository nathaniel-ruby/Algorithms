""""
Anagram Algorithm
                                        
Write a function that determines
if two strings are anagrams 
                                        
Author: Nathaniel Ruby                  
Date: 08/04/2020                        
"""

def anagramfinder(string1, string2):
    pos1 = [0]*26
    pos2 = [0]*26
    
    for i in range(len(string1)):
        alph = ord(string1[i]) - ord("a")
        pos1[alph] = pos1[alph]+1

    for i in range(len(string2)):
        alph = ord(string2[i]) - ord("a")
        pos2[alph] = pos2[alph]+1

    anagram = True
    j = 0 
    while j<26 & anagram == True:
        if pos1[j] == pos2[j]:
            j = j+1
        else:
            anagram = False
    return anagram

print(anagramfinder("peel", "leep"))
            
        
