import util.database as db

print("__name__ value: ", __name__)
def main():
    print("Query uder_definition ...\n")
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

if __name__ == '__main__':
    main()