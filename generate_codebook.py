# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:39:08 2020

@author: Jonathon Beauregard II
"""

from random import choice
#import string
from copy import copy
from sys import stdin, stderr, stdout

#All Wehrmacht models
LIST_OF_ROTORS = ['I','II','III','IV', 'V']
#Kriegsmarine M3 & M4
#LIST_OF_ROTORS = ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII']

#there are more reflectors, but this is enough
LIST_OF_REFLECTORS = ['B', 'C']

#ALPHABET=list(string.ascii_uppercase)
#Remove X to make their lives easier
ALPHABET=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

for x in range(1000):
    rotor1=choice(LIST_OF_ROTORS)
    rotor2=choice(LIST_OF_ROTORS)
    while rotor2==rotor1:
        rotor2=choice(LIST_OF_ROTORS)
    rotor3=choice(LIST_OF_ROTORS)
    while rotor3==rotor1 or rotor3==rotor2:
        rotor3=choice(LIST_OF_ROTORS)
    stdout.write("{} {} {} ".format(rotor1,rotor2,rotor3)),
    
    #Keysettings
    stdout.write("{} {} {} ".format(choice(ALPHABET),choice(ALPHABET),choice(ALPHABET))),
    
    #Plugboard
    plugboard=[]
    alphabet=copy(ALPHABET)
    for i in range(10):
        plug1=choice(alphabet)
        alphabet.remove(plug1)
        plug2=choice(alphabet)
        alphabet.remove(plug2)
        plugboard.append(plug1+plug2)
    stdout.write(" ".join(map(str, plugboard))),
    
    #reflector
    stdout.write(" {} ".format(choice(LIST_OF_REFLECTORS)))
    
    #end
    stdout.write("\n")