import pymysql
from config import DB_CONFIG

def get_connection():
    """
    Establish a connection to the MySQL database using credentials from config.py.
    """
    return pymysql.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )

def get_filtered_data(filters):
    """
    Fetch filtered data based on the provided filters from the database.
    
    Args:
        filters (dict): A dictionary of filter conditions.

    Returns:
        list: A list of dictionaries containing the filtered data.
    """
    query = "SELECT * FROM dashboard_data_table WHERE 1=1"
    params = []
    for key, value in filters.items():
        if value:
            query += f" AND {key} = %s"
            params.append(value)

    connection = get_connection()
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(query, params)
        data = cursor.fetchall()
    connection.close()
    return data
