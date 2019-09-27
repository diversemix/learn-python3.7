#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module initialisation for the flask application.
"""
import json
from flask import Flask
from logger import initLogger
from widget import WidgetService

SERVICE_CONFIG = './config.json'
LOG_PATH = './service.log'

initLogger(LOG_PATH)

def create_app():
    """ Function that initialises the application from the config. """
    _app = Flask(__name__)
    _app.service_config = {}
    with open(SERVICE_CONFIG) as data_file:
        _app.service_config = json.load(data_file)

    print(json.dumps(_app.config,
                     sort_keys=True,
                     indent=4,
                     default=str,
                     separators=(',', ': ')))

    return _app

# ----- Main function that runs the application

if __name__ == '__main__':
    app = create_app() # Create the application

    widget_service = WidgetService(app.service_config)
    app.register_blueprint(widget_service.get_api(), url_prefix='/v1')
    app.run(host="0.0.0.0", port=5000)
