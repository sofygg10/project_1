import os
import mysql.connector
from mysql.connector import Error

def insert_customers_in_bulk(df, table_name='customers'):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
        )

        if connection.is_connected():
            cursor = connection.cursor()

            insert_query = f"""
            INSERT INTO {table_name} (name, email, registration_date, country, purchased_pattern_sku)
            VALUES (%s, %s, %s, %s, %s)
            """

            customers_data = df.to_records(index=False).tolist()

            cursor.executemany(insert_query, customers_data)

            connection.commit()

            print(f"{cursor.rowcount} rows inserter successfully")

    except Error as e :
        print(f"error: {e}")
        if connection:
            connection.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

def get_all_customers ():
    try: 
        connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
        )

        if connection.is_connected():
            cursor = connection.cursor()
            select_query = """
            SELECT c.id, c.name, c.email, c.registration_date, c.country, c.purchased_pattern_sku, patterns.name, patterns.category, patterns.price,
            patterns.dificulty_level, patterns.publication_date
            FROM customers as c
            INNER JOIN patterns ON c.purchased_pattern_sku = patterns.sku
            """

            cursor.execute(select_query)
            customers = cursor.fetchall()

    except Error as e :
        print(f"error: {e}")
        
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

        return customers