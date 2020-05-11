#!/usr/bin/env python
import socket
import sys
import datetime
from enigma.machine import EnigmaMachine
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

#SERVER IP, THIS NODE
TCP_IP = '10.10.10.11'
TCP_PORT = 10000
BUFFER_SIZE = 1024
f= open("log_tcp","a+")
f.write("\n\nStarting up!!!\n")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (TCP_IP, TCP_PORT)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

#setup machine according to specs from a daily key sheet:
#medium-hard, army level, only initial three three
machine = EnigmaMachine.from_key_sheet(
       rotors='II I III',
       reflector='B',
       plugboard_settings='KE JD MN LS OW')

# Wait for a connection
print('waiting for a connection')
connection, client_address = sock.accept()
print('connection from', client_address)

while 1:
	#set machine to todays setting
	machine.set_display('ABC')

	# get data
	MESSAGE = connection.recv(BUFFER_SIZE).decode()
	if not MESSAGE: break

	f.write(str(datetime.datetime.now())+"\n")
	f.write(str(machine.get_display()) + "\n")
	f.write("received data from client:"+ MESSAGE +"\n")

	#decrypt message
	ED = machine.process_text(MESSAGE)
	f.write("received plain data from client:"+ ED +"\n")

	#set machine to todays setting
	machine.set_display('ABC')
	
	#prepare message
	MESSAGE=(ED+", Yes sir.")
	EM = machine.process_text(MESSAGE)
	f.write("sending plain message: "+ MESSAGE+"\n")
	f.write("sending enigm message: "+ EM+"\n")

	# Send data
	connection.sendall(EM.encode())

	#cleanup and prep for next message
	f.write("\n")
	f.flush()


# Clean up the connection
connection.close()
f.close()
