#!/usr/bin/env python
import socket
import sys
import time
import datetime
from enigma.machine import EnigmaMachine
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine
from collections import deque

#SERVER IP
TCP_IP = '10.10.10.11'
TCP_PORT = 10000
BUFFER_SIZE = 1024
f= open("log_tcp","a+")
fx= open("keys/log_tcp", "a+")


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (TCP_IP, TCP_PORT)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

#messages that are to be sent
queue = deque(["She made the room dark and slept; she awoke and made the room light; she ate and exchanged ideas with her friends, and listened to music and attended lectures; she make the room dark and slept. Above her, beneath her, and around her, the Machine hummed eternally; she did not notice the noise, for she had been born with it in her ears. The earth, carrying her, hummed as it sped through silence, turning her now to the invisible sun, now to the invisible stars. She awoke and made the room light. The Secret word is electroboom."])


#setup machine according to specs from a daily key sheet:
#medium-hard, army level, only initial three rotors
machine = EnigmaMachine.from_key_sheet(
       rotors='II I III',
       reflector='B',
       plugboard_settings='KE JD MN LS OW')



while 1:

	#set machine to todays setting
	machine.set_display('ABC')

	#write info to log
	f.write(str(datetime.datetime.now()) + "\n")
	f.write(str(machine.get_display()) + "\n")
	fx.write("Rotor position: "+str(machine.get_display()) + "\n")

	#pick a message and encrypt it
	MESSAGE = queue.popleft()
	EM = machine.process_text(MESSAGE)

	#write info to log
	f.write("sending plain message: "+ MESSAGE+"\n")
	f.write("sending enigm message: "+ EM+"\n")
	fx.write("sending enigm message: "+ EM+"\n")

	# Send data
	sock.sendall(EM.encode())

	#set machine to todays setting
	machine.set_display('ABC')
	fx.write("Rotor position: "+str(machine.get_display()) + "\n")
	f.write(str(machine.get_display()) + "\n")

	# Look for the response
	data = sock.recv(BUFFER_SIZE).decode()
	
	#decrypt message
	ED = machine.process_text(data)

	f.write("received enigm from server: "	+ data+"\n")
	fx.write("received enigm from server: "+ data+"\n")
	f.write("received plain from server: "+ ED+"\n")

	#cleanup and prep for next message
	f.write("\n")
	fx.write("\n")
	f.flush()
	fx.flush()
	
	#recycle message for later use
	queue.append(MESSAGE)
	time.sleep(60)


print('closing socket')
sock.close()
