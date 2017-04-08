# zabbix-oio

These scripts use the default 'OPENIO' NS. You can modify it to fit your needs in 'userparameter_openio.conf' and 'zabbix-oiosds-discover.py'  

This tamplate only discovers oio SDS services and track the scores. Waiting for 1704 so that It can list and get account metrics  

## DEBIAN
```
wget https://github.com/Mixton/zabbix-oio/userparameter_openio.conf -O /etc/zabbix/zabbix_agentd.conf.d/userparameter_openio.conf  
wget https://github.com/Mixton/zabbix-oio/zabbix-oiosds-discover.py -O /usr/local/bin/zabbix-oiosds-discover.py  
chmod +x /usr/local/bin/zabbix-oiosds-discover.py  
systemctl restart zabbix-agent.service  
```

import template 'zbx_oiosds_template.xml' and add it to your host  

## CENTOS/RedHat
```
wget https://github.com/Mixton/zabbix-oio/userparameter_openio.conf -O /etc/zabbix_agentd.conf.d/userparameter_openio.conf  
wget https://github.com/Mixton/zabbix-oio/zabbix-oiosds-discover.py -O /usr/local/bin/zabbix-oiosds-discover.py  
chmod +x /usr/local/bin/zabbix-oiosds-discover.py  
systemctl restart zabbix-agent.service  
```

import template 'zbx_oiosds_template.xml' and add it to your host 
