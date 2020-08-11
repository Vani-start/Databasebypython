#!/bin/python

#DELETE
Delete_Query="DELETE FROM users WHERE userid=104"
my_cursor.execute(Delete_Query)
db.commit()
