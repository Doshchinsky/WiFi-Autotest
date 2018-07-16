# Import section

import numpy as np
import pexpect
import re

# Var section

IPaddr = ['192.168.42.178','172.16.27.62','192.168.2.1','172.16.42.17']
username = ['admin', 'techsupport']
password = ['vl-qwerty', 'password']
result_file = "data.txt"

# Func section

def readfile(filename):
	with open(filename, 'r') as _file:
		return _file.readlines()

def writefile(data, filename):
	with open(filename, 'w+') as _file:
		for index in range(len(data)):
			if data[index] is not None:
				_file.write(data[index] + '\n')

def telnet_logging(IP, login, passwd):
	stream = pexpect.spawn('telnet', [IP])
	
	stream.expect('[lL]ogin')
	stream.sendline(login)

	stream.expect('[pP]assword')
	stream.sendline(passwd)

	stream.expect('#')
	return stream 

def ssh_logging(IP, passwd):
	stream = pexpect.spawn('ssh', [IP])

	stream.expect('[pPassword]')
	stream.sendline(passwd)
	stream.expect('$')
	return stream

def run_iperf():

# Code section
