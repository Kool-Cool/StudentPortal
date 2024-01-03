import psycopg2
DATABASE_URL = 'posrgerass@user'

def execute_query(query, values=None):
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"Error executing query: {e}")
    finally:
        cursor.close()
        connection.close()




