import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    command1 = "CREATE TABLE cities (
            cityName SERIAL PRIMARY KEY,
            stateName VARCHAR(255) NOT NULL,
            cityPopulation int(255) NOT NULL,
            latitude real(255) NOT NULL,
            longitude real(255) NOT NULL
        )"

    command2 = "CREATE TABLE stateAbb (
            abbreviation SERIAL PRIMARY KEY,
            stateName VARCHAR(255) NOT NULL
        )"
    

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
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