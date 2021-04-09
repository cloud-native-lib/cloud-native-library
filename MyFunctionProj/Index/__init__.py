import logging
import azure.functions as func
from fonctions.fonctions import index,jinja_info


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(index(),status_code=200, mimetype='text/html')