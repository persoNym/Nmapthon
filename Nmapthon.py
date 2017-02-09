#! usr/bin/python
# coding utf-8

import sys, os
from socket import*
from datetime import datetime

print """         (\ /)
        c( . .) ~< NMAPTHON ~ A NMAP PYTHON PORT SCANNER >"""

common_ports = {
	    '20': 'FTP',
	    '21': 'FTP',
	    '22': 'SSH',
	    '23': 'TELNET',
	    '25': 'SMTP',
	    '53': 'DNS',
	    '69': 'TFTP',
	    '79': 'FINGER',
	    '80': 'HTTP',
	    '88': 'KEREBEROS',
	    '109': 'POP2',
	    '110': 'POP3',
	    '123': 'NTP',
	    '137': 'NETBIOS-NS',
	    '138': 'NETBIOS-DGM',
	    '139': 'NETBIOS-SSN',
	    '143': 'IMAP',
	    '156': 'SQL-SERVER',
	    '194': 'INTERNET RELAY CHAR (IRC)',
	    '389': 'LDAP',
	    '443': 'HTTPS',
	    '546': 'DHCP-CLIENT',
	    '547': 'DHCP-SERVER',
	    '995': 'POP3-SSL',
	    '993': 'IMAP-SSL',
	    '2086': 'WHM/CPANEL',
	    '2087': 'WHM/CPANEL',
	    '2082': 'CPANEL',
	    '2083': 'CPANEL',
	    '3306': 'MYSQL',
	    '8443': 'PLESK',
	    '10000': 'VIRTUALMIN/WEBMIN'
        }
Host = raw_input('Input IP address you would like to scan: ')
#StartPort = input('Input starting port: ')
#EndPort = input('Input ending port: ')

print "Commencing Scan"

#The start time of the scan
TimeStart = datetime.now()

for port in range(1 - 1024):
    soc=socket(AF_INET, SOCK_STREAM)          # Creates a socket
    if soc.connect_ex(Host,port)==0:       # If connection to port was successful,then returns 0
        for ports in common_ports:
            CommonPorts = common_ports[ports]
            print "Port: ", port, "Service: ", CommonPorts, " is open"  # Prints open port
    soc.close()                               # Closes socket

print "Scanning completed !! "

#The end time of the scan
TimeEnd = datetime.now()

#The length the scan took
TimeDuration = TimeEnd - TimeStart
print "Scanning Duration is: ", TimeDuration


