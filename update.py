#!/bin/python

#UPDATE
Update_query="UPDATE users SET username='ems' WHERE userid=104"
my_cursor.execute(Update_query)
db.commit()
