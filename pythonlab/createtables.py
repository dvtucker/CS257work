import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    command1 = """CREATE TABLE cities (
            cityName text,
            stateName text NOT NULL,
            cityPopulation int NOT NULL,
            latitude real NOT NULL,
            longitude real NOT NULL
        )"""

    command2 = """CREATE TABLE stateAbb (
            abbreviation text,
            stateName text NOT NULL
        )"""
    

    conn = None
    try:
        # read the connection parameters
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="tuckerd",
            user="tuckerd",
            password="carpet664winter")

        cur = conn.cursor()
        # create table one by one
        cur.execute(command1)
        cur.execute(command2)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
