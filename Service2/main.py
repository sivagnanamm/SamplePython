import logging
from flask import request, g, jsonify, Flask

from service.service2_service import Service2


app = Flask('Service2')


def health_check():
    return {"Status": "Service Running Successfully"}


def list_endpoint():
    service = Service2()
    return service.list_item()


def get_endpoint():
    service = Service2()
    return service.get_item()


def create_endpoint():
    service = Service2()
    return service.create_item()


app.add_url_rule(rule='/health', endpoint='health-check', view_func=health_check, methods=['GET'])
app.add_url_rule(rule='/list', endpoint='list-endpoint', view_func=list_endpoint, methods=['GET'])
app.add_url_rule(rule='/', endpoint='get-endpoint', view_func=get_endpoint, methods=['GET'])
app.add_url_rule(rule='/', endpoint='create-endpoint', view_func=create_endpoint, methods=['POST'])

