import psycopg2
DATABASE_URL = 'postgres://nnszspoo:IxIAqh_7_71Of3JAhMMN9DGAmLJlhPOv@john.db.elephantsql.com/nnszspoo'

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




