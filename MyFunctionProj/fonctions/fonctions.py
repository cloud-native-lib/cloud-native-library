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
    html_list_books = """<a class="btn btn-outline-secondary" href="https://cloudlibrary.azurewebsites.net/api/book?name="""
    for book in books:
        if book != books[-1]:
            html_list_books += """"""+book+"""">"""+book+"""</a> <a class="btn btn-outline-secondary" href="https://cloudlibrary.azurewebsites.net/api/book?name="""
        else:
            html_list_books += book
            # html_list_books += "</h5>"
            html_list_books += "</a>"
    return html_list_books


def result_html():
    result = """
         <html>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>Cloud library Azure</title>
        <link rel="stylesheet" href="https://bootswatch.com/4/sketchy/bootstrap.min.css" />
        <br><br><head>""" + my_css()+"""
        <div class="jumbotron">
        <h1 class="display-3">Cloud library Azure !</h1>
        <p class="lead">Voici la liste des livres disponible</p>
        <hr class="my-4">
            <p>Clickez sur un livre pour avoir plus d'informations et
            son lien de téléchargement</p>
        <p class="lead">

        """ + liste_html() + """
    </p>
    </div>
        </head>
        <body> <div>
            <center>
            <p>
                <ul></ul>
            </p></center><div>
        </body>
        </html>
        """
    return result

def my_css():
    msg="""<style>
         h1
        {
            font-size: 3em;
            text-align:left;
        }
        h3
        {
            text-align:center;
        }
        #btn_book{
            margin:7px;
        }
        a.btn.btn-outline-secondary {
            margin:10px;
           min-width: 210px;
            max-width: 210px;
        }
        
        </style>"""
    return msg


def index():
    result = """
        <html>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>Cloud library Azure</title>
        <link rel="stylesheet" href="https://bootswatch.com/4/sketchy/bootstrap.min.css" />
        <br><br><head>""" + my_css()+"""
        <div class="jumbotron">
        <h1 class="display-3">Cloud library Azure !</h1>
        <p class="lead">Bienvenue sur notre librairie</p>
        <hr class="my-4">
            <p>Clickez sur le boutton pour voir nos livres disponibles</p>
        <p class="lead">
            <a class="btn btn-primary btn-lg" href="https://cloudlibrary.azurewebsites.net/api/httptrigger" role="button">Livres</a>
    </p>
    </div>
        </head>
        <body> <div>
            <center>
            <p>
                <ul></ul>
            </p></center><div>
        </body>
        </html>
        """
    return result
