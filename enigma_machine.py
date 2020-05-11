#!/usr/bin/env python
import copy
from enigma.machine import EnigmaMachine

print("Starting up machine...")

D = int(input("What is the day for this message? :"))

with open('Schlusselblatt', 'r') as f:
	machine = EnigmaMachine.from_key_file(f, day=D)
	machine1 = copy.deepcopy(machine)

	#pick a message and encrypt it
	MESSAGE = input("What is the message? :")
	EM = machine.process_text(MESSAGE)
	print("Output message = ", EM , "\n")
	
	#decrypt message, just to double check
	#we are using a copy of the machine, with the original configurations, to check the message to ensure it is functioning.
	ED = machine1.process_text(EM)
	print("Input message = ", ED, "\n")

print('Completed')
