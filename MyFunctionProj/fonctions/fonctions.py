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

    
def list_book():
    
    request = cursor.execute("""SELECT titre
    From library""")
    result = cursor.fetchall()
    res =[]
    for row in result:
        res.append(row["titre"])
    # return json.dumps(result[0]["titre"])
    return res
   
        

def liste_html():
    books = list_book()
    html_list_books = """<span class="badge badge-secondary">"""
    for book in books:
        if book != books[-1]:
            html_list_books += book
            html_list_books += """</span><br><br><span class="badge badge-secondary">"""
        else:
            html_list_books += book
            # html_list_books += "</h5>"
            html_list_books += "</span>"
    return html_list_books


def result_html():
    result = """
        <html>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>Cloud library Azure</title>
        <link rel="stylesheet" href="https://bootswatch.com/4/sketchy/bootstrap.min.css" />
        <br><br><head><center>     <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor03" aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button><h3>Voici la liste des livres disponible</h3>
        </center> <br><br>
        </head>
        <body> <div>
          <center>
            <p>
                <ul>""" + liste_html() + """</ul>
            </p></center><div>
        </body>
        </html>
        """
    return result