#!/usr/bin/python
import os
import subprocess
import shlex
import json
import socket
import netifaces

if __name__ == "__main__":
    #hostname = socket.gethostname()
    ifaces = netifaces.interfaces()
    ifacesbanned = ('lo')
    ifaces = (iface for iface in ifaces if not any(ifacebanned in iface for ifacebanned in ifacesbanned))
    for iface in ifaces:
        addrs = netifaces.ifaddresses(iface)
        break
    hostname = addrs[netifaces.AF_INET][0]['addr']
    cmd = '/usr/bin/oio-cluster -r OPENIO  '
    #cmd = raw_input("shell:")
    args = shlex.split(cmd)
    output,error = subprocess.Popen(args,stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
    #print error
    output = output.split('\n')
    servs = []
    services = (service for service in output
                if (hostname in service))
    for service in services:
        service = ' '.join(service.split('|'))
        serv = service.split(' ')[1] + "-" + service.split(' ')[2]
        #serv = ''.join(serv.split(':'))
        servs.append(serv)
    data = [{"{#SERVICENAME}": service} for service in servs]
    print(json.dumps({"data": data}, indent=4))
