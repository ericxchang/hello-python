import psycopg2


class Database:
    def __init__(self, **kwargs):
        self.connect(**kwargs)

    def connect(self, **kwargs):
        try:
            self.connection = psycopg2.connect(**kwargs)
        except(Exception, psycopg2.Error) as error:
            print("Failed to connect to database: ", error)

    def query(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except(Exception, psycopg2.Error) as error:
            print("Error to fetch data", error)
        finally:
            if (cursor):
                cursor.close()

    def close(self):
        if (self.connection):
            self.connection.close()
