import logging

import azure.functions as func
from fonctions.fonctions import my_css,index


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(index(),status_code=200, mimetype='text/html')

