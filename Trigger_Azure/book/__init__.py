import logging
from fonctions.fonctions import jinja_list_book,jinja_info
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    if not name : 
        return func.HttpResponse(jinja_list_book(),status_code=200, mimetype="text/html")
    if name:
        return func.HttpResponse(jinja_info(name), status_code=200, mimetype='text/html')

