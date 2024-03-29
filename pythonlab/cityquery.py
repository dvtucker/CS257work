import psycopg2

def test_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="tuckerd",
        user="tuckerd",
        password="carpet664winter")

    cur = conn.cursor()

    sql = "SELECT cityName FROM cities WHERE cityName = 'Northfield' "
    
    cur.execute( sql )

    result = cur.fetchall()
    if result is None:
        print("Northfield is not present in the database.")
    else:
        print(result)


def test_query_two():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="tuckerd",
        user="tuckerd",
        password="carpet664winter")

    cur = conn.cursor()

    sql = "SELECT cityName FROM cities ORDER BY cityPopulation DESC LIMIT 1 "
    
    cur.execute( sql )

    result = cur.fetchone()
    print("The city with the largest population is: ")
    print(result)


def test_query_three():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="tuckerd",
        user="tuckerd",
        password="carpet664winter")

    cur = conn.cursor()

    sql = "SELECT cityName FROM cities WHERE stateName = 'Minnesota' ORDER BY cityPopulation LIMIT 1 "
    
    cur.execute( sql )

    result = cur.fetchone()
    print("The city in Minnesota with the smallest population is: ")
    print(result)

def test_query_four():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="tuckerd",
        user="tuckerd",
        password="carpet664winter")

    cur = conn.cursor()

    #finds largest latitude
    sql = "SELECT cityName FROM cities ORDER BY latitude DESC LIMIT 1 "
    cur.execute( sql )
    result = cur.fetchone()
    print("The city that is furthest North is: ")
    print(result)

    #finds smallest latitude
    sql = "SELECT cityName FROM cities ORDER BY latitude LIMIT 1 "
    cur.execute( sql )
    result = cur.fetchone()
    print("The city that is furthest South is: ")
    print(result)

    #finds smallest longitude
    sql = "SELECT cityName FROM cities ORDER BY longitude LIMIT 1 "
    cur.execute( sql )
    result = cur.fetchone()
    print("The city that is furthest West is: ")
    print(result)

    #finds largest longitude
    sql = "SELECT cityName FROM cities ORDER BY longitude DESC LIMIT 1 "
    cur.execute( sql )
    result = cur.fetchone()
    print("The city that is furthest East is: ")
    print(result)


def test_query_five():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="tuckerd",
        user="tuckerd",
        password="carpet664winter")

    cur = conn.cursor()

    state_name = input("Enter a state: ")

    # If input is an abbreviation, look up the full state name
    if len(state_name) == 2:
        state_name = state_name.upper()  # Convert to uppercase 
        cur.execute("SELECT stateName FROM stateAbb WHERE abbreviation='" + state_name + "';")
        state_result = cur.fetchone()
        if state_result is not None:
            state_name = state_result[0]

    # get the total city population for the state
    cur.execute("SELECT SUM(cityPopulation) FROM cities WHERE stateName='" + state_name + "';")
    
    total_pop = cur.fetchone()[0]

    if total_pop is not None:
        print("The total population is:", total_pop)
    else:
        print("State not found")

test_query_one()
test_query_two()
test_query_three()
test_query_four()
test_query_five()
   
