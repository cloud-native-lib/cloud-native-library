import logging
import azure.functions as func
from fonctions.fonctions import list_book,liste_html, result_html


def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a request.')
        return func.HttpResponse(result_html(),status_code=200, mimetype='text/html')


