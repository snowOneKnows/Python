#!/usr/bin/env python3
# Port scanning in python using builtins 
# Imports 
import socket

# Class 

class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = [];


    def __repr__(self):
        return 'Scanner: {}'.format(self.ip)

    def add_port(self, port):
        self.open_ports.append(port)
        print("IP has port Open: {} {}".format(self.ip,port))


    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            # adds 1 to end of range due to range always dropping on the right value
            if self.is_open(port):
                self.add_port(port)


    def is_open(self, port):
        """" check if socket is open. this will attempt to connect if is open retun true or false. """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0

    def write(self, filepath):
        """" Writes to file saving ports as new line. """
        openport = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(openport))

# Program starts here. 
# changes and scopes
# ------------------
# 1. Add IP, range to args list instead of hard coding as nothing should be hard coded 
# 2. include banner reading 
# 3. Add optional flag for saving to file and adding filename or just print to screen.

def main():
    ip = '192.168.50.1'
    scanner = Scanner(ip)
    scanner.scan(50, 85)
    scanner.write('ports.txt')

if __name__ == '__main__':
    main()