import mysql.connector
import json
import os
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient
from uploadbook import list_blob



config_sql = {
  'host':os.environ['HOST_SQL_AZURE'],
  'user':os.environ['USER_SQL_AZURE'],
  'password':os.environ['PASSWORD_SQL_AZURE'],
  'database':os.environ['DATABASE_SQL_AZURE'],
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': os.environ["SSL_CA_SQL_AZURE"]}

conn = mysql.connector.connect(**config_sql)
cursor = conn.cursor(dictionary=True)
    
def list_book():
    
  cursor.execute("""SELECT titre
  From library""")
  result = cursor.fetchall()
  return result

def list_book_like(titre):

  cursor.execute("""SELECT titre
  From library WHERE titre like "%s" """, (titre))
  result = cursor.fetchall()
  return result

def title_in_database(title):

  for book in list_book():
    if title.lower() in book.values():
      return True
  return False

def blob_exists(args_cible, containerclient):
  
    blob_names = list_blob(args_cible, containerclient)
    for blob in blob_names:
      if args_cible == blob:
        return True
    return False

def print_blob_name(blob_names):
  for blob_name in blob_names:
    print(blob_name)

def set_blobclient(containerclient, args_cible):
  return containerclient.get_blob_client(os.path.basename(args_cible))

def ask_blob_info(containerclient, args_cible):

  book_title = input("Quel est le titre de votre livre : ").lower()
  while title_in_database(book_title):
    book_title = input("Ce livre existe déjà, veuillez réesayer : ").lower()
  args_cible = args_cible.replace(".\\", "" )
  while blob_exists(args_cible, containerclient):
    args_cible = input("Ce blob exists déjà veuillez choisir un nouveau fichier : ")
  containerclient = set_blobclient(containerclient, args_cible)
  print("Connection established")
  book_gender = input("Quel est le genre de livre :").lower()
  return book_title, book_gender, containerclient, args_cible
 
def upload_to_database(book_title, book_gender):

  blob_url= f'https://cloudlibrary2.blob.core.windows.net/library/{book_title}.txt'
  cursor.execute("""INSERT INTO library (titre,gender,urlblob) VALUES (%s, %s,%s)"""
                  ,(book_title,book_gender,blob_url))
  conn.commit()
  






