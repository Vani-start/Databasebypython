#!/bin/python

my_cursor.execute("SELECT * FROM users WHERE username = 'enm' OR username = 'nms'")
new_val = my_cursor.fetchall()
for val in new_val:
    print(val)

