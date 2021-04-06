import logging
import mysql.connector
import json
import os
import re

from blobTrigger.blob import Blob
import blobTrigger.db_functions as dbf
import azure.functions as func

config_sql = {
  'host':os.environ['HOST_SQL_AZURE'],
  'user':os.environ['USER_SQL_AZURE'],
  'password':os.environ['PASSWORD_SQL_AZURE'],
  'database':os.environ['DATABASE_SQL_AZURE'],
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': os.environ["SSL_CA_SQL_AZURE"]}


def main(newBlob: func.InputStream):

    # Create blob instance
    blob = Blob(newBlob)

    # create dictionnary with word occurrencies
    # parse name
    number_of_words = json.dumps(blob.word_occurrences())
    # title = re.findall(r"[\w']+", newBlob.name)[1]
    logging.info(number_of_words)
    
    # Connect to Azure database and update table information
    conn = mysql.connector.connect(**config_sql)
    logging.info(conn)
    dbf.load_info(conn, number_of_words)
    conn.close()
