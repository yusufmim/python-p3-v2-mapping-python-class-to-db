#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

d1 = Department(name="Engineering", location="Building 1")
print("Before save:", d1)

d1.save()
print("After save:", d1)

ipdb.set_trace()
