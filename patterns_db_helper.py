import os
import mysql.connector
from mysql.connector import Error

def insert_patterns_in_bulk(df, table_name='patterns'):
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
            INSERT INTO {table_name} (name, sku, category, price, dificulty_level, publication_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            patterns_data = df.to_records(index=False).tolist()

            cursor.executemany(insert_query, patterns_data)

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

def get_all_patterns():
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
            SELECT p.id, p.name, p.sku, p.category, p.price, p.dificulty_level, p.publication_date FROM patterns as p;
            """

            cursor.execute(select_query)
            patterns = cursor.fetchall()

    except Error as e :
        print(f"error: {e}")
        
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

        return patterns
        


            