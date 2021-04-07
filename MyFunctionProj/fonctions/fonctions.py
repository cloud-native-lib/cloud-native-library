import os
import mysql.connector
import json
from jinja2 import Template


config_sql = {
  'host':os.environ['HOST_SQL_AZURE'],
  'user':os.environ['USER_SQL_AZURE'],
  'password':os.environ['PASSWORD_SQL_AZURE'],
  'database':os.environ['DATABASE_SQL_AZURE'],
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': os.environ["SSL_CA_SQL_AZURE"]}


conn = mysql.connector.connect(**config_sql)
cursor = conn.cursor(dictionary=True)


def jinja_list_book():

    books= list_book()
    with open('list_book.html') as file_:
        template = Template(file_.read())
    result = template.render(books=books)
    return result


def list_book():
    
    request = cursor.execute("""SELECT titre
    From library""")
    result = cursor.fetchall()
    res =[]
    for row in result:
        res.append(row["titre"])
    # return json.dumps(result)
    return res


def info_book(titre):



def index():

    html = open(f"index.html", "r").read()
    return html
