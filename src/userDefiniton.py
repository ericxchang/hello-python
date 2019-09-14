from .database import Database

db = Database(
    user="dashboard",
    password="dashboard",
    host="localhost",
    port="5432",
    database="dashboard"
)

result = db.query("select * from operations.user_definition")

for row in result:
    print(row, "\n")

db.close()