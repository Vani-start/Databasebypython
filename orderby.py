#!/bin/python
Order_by="Select * FROM users LIMIT 2 OFFSET 2"
my_cursor.execute(Order_by)
new=my_cursor.fetchall()

for rw in new:
    print(rw)
