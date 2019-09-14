import sys

from gevent import os

sys.path.append(os.getcwd())
import util.database as db


def fetch_user_definition():
    print("Query user_definition ...\n")
    my_db = db.Database(
        user="dashboard",
        password="dashboard",
        host="localhost",
        port="5432",
        database="dashboard"
    )

    result = my_db.query("select * from operations.user_definition")

    for row in result:
        print(row, "\n")

    my_db.close()


if __name__ == "__main__":
    fetch_user_definition()
