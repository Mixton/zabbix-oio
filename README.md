# zabbix-oio

- oio sds = 1610
- zabbix >= 2.0

These scripts use the default 'OPENIO' NS. You can modify it to fit your needs in 'userparameter_openio.conf' and 'zabbix-oiosds-discover.py'  

This tamplate only discovers oio SDS services and tracks the scores. Waiting for 1704 so that it can list and get account metrics  

To monitor oio-sds nodes you might want to use a template that gives you disks info too. This one works well: https://github.com/grundic/zabbix-disk-performance

## DEBIAN
On each oio-sds zabbix agent hosts:
```
wget https://raw.githubusercontent.com/Mixton/zabbix-oio/master/userparameter_openio.conf -O /etc/zabbix/zabbix_agentd.conf.d/userparameter_openio.conf  
apt-get install python-netifaces
wget https://raw.githubusercontent.com/Mixton/zabbix-oio/master/zabbix-oiosds-discover.py -O /usr/local/bin/zabbix-oiosds-discover.py  
chmod +x /usr/local/bin/zabbix-oiosds-discover.py  
systemctl restart zabbix-agent.service  
```

import template 'zbx_oiosds_template.xml' and add it to your host  

## CENTOS/RedHat
On each oio-sds zabbix agent hosts:
```
wget https://raw.githubusercontent.com/Mixton/zabbix-oio/master/userparameter_openio.conf -O /etc/zabbix_agentd.conf.d/userparameter_openio.conf  
yum install -y python-netifaces.x86_64
wget https://raw.githubusercontent.com/Mixton/zabbix-oio/master/zabbix-oiosds-discover.py -O /usr/local/bin/zabbix-oiosds-discover.py  
chmod +x /usr/local/bin/zabbix-oiosds-discover.py  
systemctl restart zabbix-agent.service  
```

import template 'zbx_oiosds_template.xml' and add it to your host 
