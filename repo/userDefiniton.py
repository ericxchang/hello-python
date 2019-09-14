import sys
from gevent import os
sys.path.append(os.getcwd())
import util.database as db

print("Query user_definition ...\n")
myDB = db.Database(
    user="dashboard",
    password="dashboard",
    host="localhost",
    port="5432",
    database="dashboard"
)

result = myDB.query("select * from operations.user_definition")

for row in result:
    print(row, "\n")

myDB.close()
