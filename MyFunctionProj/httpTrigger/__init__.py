import logging
from fonctions.fonctions import list_book
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(list_book(), status_code=200, mimetype="application/json")
