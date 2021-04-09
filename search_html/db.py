import os
import mysql.connector

config_sql = {
  'host':os.environ['HOST_SQL_AZURE'],
  'user':os.environ['USER_SQL_AZURE'],
  'password':os.environ['PASSWORD_SQL_AZURE'],
  'database':os.environ['DATABASE_SQL_AZURE'],
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': os.environ["SSL_CA_SQL_AZURE"]}

conn = mysql.connector.connect(**config_sql)
cursor = conn.cursor(dictionary=True)

def all_titles():
    request = """
    SELECT titre
    FROM library
    """
    cursor.execute(request)
    return cursor.fetchall()
