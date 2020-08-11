#!/bin/python

INSERT query
Insert_query = "INSERT INTO users (username,userid) VALUES (%s,%s)"

values = [("enm",101),("nms",102),("stms",103),("nms",104),("bgf",105)]
my_cursor.executemany(Insert_query,values)
db.commit()
