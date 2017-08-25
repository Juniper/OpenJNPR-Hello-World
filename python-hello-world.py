# Copyright 2017, Juniper Networks Pvt Ltd.
# All rights reserved.
#!/usr/bin/env python

from ncclient import manager
from ncclient.xml_ import *
from lxml import etree as etree
import time

def connect(host, port, user, password, source):
    conn = manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
            device_params = {'name':'junos'},
            hostkey_verify=False)

    rpc = new_ele('get-system-information')
    result = conn.rpc(rpc)
    print result

if __name__ == '__main__':
    connect('X.X.X.X', 22, 'username', 'password', 'candidate')
