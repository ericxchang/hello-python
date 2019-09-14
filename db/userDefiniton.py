import database as db

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