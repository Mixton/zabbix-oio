# zabbix-oio

## DEBIAN
```
wget https://github.com/Mixton/zabbix-oio/userparameter_openio.conf -O /etc/zabbix/zabbix_agentd.conf.d/userparameter_openio.conf  
wget https://github.com/Mixton/zabbix-oio/zabbix-oiosds-discover.py -O /usr/local/bin/zabbix-oiosds-discover.py  
chmod +x /usr/local/bin/zabbix-oiosds-discover.py  
systemctl restart zabbix-agent.service  
```

import template  

## CENTOS/RedHat
```
wget https://github.com/Mixton/zabbix-oio/userparameter_openio.conf -O /etc/zabbix_agentd.conf.d/userparameter_openio.conf  
wget https://github.com/Mixton/zabbix-oio/zabbix-oiosds-discover.py -O /usr/local/bin/zabbix-oiosds-discover.py  
chmod +x /usr/local/bin/zabbix-oiosds-discover.py  
systemctl restart zabbix-agent.service  
```

import template  
