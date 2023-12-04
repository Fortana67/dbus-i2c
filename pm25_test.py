#!/usr/bin/env python

import os
import sys
from script_utils import SCRIPT_HOME
sys.path.insert(1, os.path.join(os.path.dirname(__file__), f"{SCRIPT_HOME}/ext"))
from pm25_i2c import PM25_I2C

pm25 = PM25_I2C(1)
print(pm25.read())
