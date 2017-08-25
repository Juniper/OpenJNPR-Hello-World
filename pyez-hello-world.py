# Copyright 2017, Juniper Networks Pvt Ltd.
# All rights reserved.
#

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='X.X.X.X', user='username', password='password')
dev.open()
print(dev.facts)
dev.close()
