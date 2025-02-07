import os
import sys
import logging
import zeroconf
from zeroconf import Zeroconf

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from boschshcpy import SHCSession, SHCDeviceHelper

# logging.basicConfig(level=logging.DEBUG)

# Create session with additional zeroconf info
zeroconf = Zeroconf()
session = SHCSession(
    controller_ip="192.168.1.6", certificate='../keystore/dev-cert.pem', key='../keystore/dev-key.pem', zeroconf=zeroconf)
zeroconf.close()

for device in session.devices:
    device.summary()

for room in session.rooms:
    room.summary()

for scenario in session.scenarios:
    scenario.summary()

session.intrusion_system.summary()

session.information.summary()