import logging
import azure.functions as func
from fonctions.fonctions import jinja_list_book


def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a request.')
        return func.HttpResponse(jinja_list_book(),status_code=200, mimetype="text/html")

