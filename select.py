#!/bin/python
Select_query="CREATE TABLE users (username VARCHAR(255), userid INTEGER(25))"
my_cursor.execute(Select_query)
for each in my_cursor:
    print(each)

