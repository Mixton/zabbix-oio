#!/usr/bin/python
import os
import subprocess
import shlex
import json
import socket
import netifaces
import requests
import argparse
import textwrap

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='zabbix-oiosds-discover.py', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
                        TODO
                        '''), epilog="e.g. zabbix-oiosds-discover.py --ns <OIO-NS> -p <OIO-PROXY port> -s <service>")
    parser.add_argument('--ns', help='set oio-ns', required=False, default='OPENIO')
    parser.add_argument('-p', '--port', help='set oio-proxy port', required=False, default='6006')
    parser.add_argument('-s', '--servicename', help='servicename = <service_type-service_id>', required=False)
    parser.add_argument('--getscore', help='get score (need servicename to be set)', required=False, action='store_true')
    parser.add_argument('--getstatus', help='get status (need servicename to be set)', required=False, action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s v0.1')
    args = parser.parse_args()

    NS = args.ns
    PROXY_PORT = args.port

    services_list = ('account', 'rdir', 'meta0', 'meta1', 'meta2', 'rawx')

    #hostname = socket.gethostname()
    ifaces = netifaces.interfaces()
    ifacesbanned = ('lo')
    ifaces = (iface for iface in ifaces if not any(ifacebanned in iface for ifacebanned in ifacesbanned))
    for iface in ifaces:
        addrs = netifaces.ifaddresses(iface)
        break
    hostname = addrs[netifaces.AF_INET][0]['addr']

    if args.servicename:
        service = args.servicename.split('-')[0]
        service_id = args.servicename.split('-')[1]
        url = "http://%s:%s/v3.0/%s/conscience/list?type=%s"%(hostname, PROXY_PORT, NS, service)
        cmd = "/usr/bin/curl -XGET %s"%url
        cmd_args = shlex.split(cmd)

        try:
            output,error = subprocess.Popen(cmd_args,stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
        except Exception, e:
            if args.getscore:
                print(0)
            elif args.getstatus:
                print(False)
        else:

            output = json.loads(output)

            if args.getscore:
                score = 0
                for host in output:
                    if service_id in host['addr']:
                        score = host['score']


                print(score)

            elif args.getstatus:
                active = False
                for host in output:
                    if service_id in host['addr']:
                        active = host['tags']['tag.up']


                print(active)

    else:

        services = []

        for service in services_list:
            url = "http://%s:%s/v3.0/%s/conscience/list?type=%s"%(hostname, PROXY_PORT, NS, service)
            cmd = "/usr/bin/curl -XGET %s"%url
            cmd_args = shlex.split(cmd)
            try:
                output,error = subprocess.Popen(cmd_args,stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
            except Exception, e:
                print(e)
            else: 
                output = json.loads(output)
                for host in output:
                    if hostname in host['addr']:
                        serv = "%s-%s"%(service, host['addr'])
                        services.append(serv)

        if services:
            data = [{"{#SERVICENAME}": service} for service in services]
            print(json.dumps({"data": data}, indent=4))
