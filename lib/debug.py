#lib/testing/debug.py
#!/usr/bin/env python3


from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Reset table
Department.drop_table()
Department.create_table()

# Create & save new department
payroll = Department("Payroll", "Building A, 5th Floor")
print("Before save:", payroll)
payroll.save()
print("After save:", payroll)

# Create using class method
hr = Department.create("Human Resources", "Building B, 2nd Floor")
print("Created HR:", hr)

# Update
payroll.location = "Building C, 1st Floor"
payroll.update()
print("After update:", payroll)

# Delete
hr.delete()
print("HR deleted")

ipdb.set_trace()
