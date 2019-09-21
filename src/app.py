#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module initialisation for the flask application.
"""
import json
from flask import Flask
from logger import initLogger
from flask_sqlalchemy import SQLAlchemy
from test_app import Service

SERVICE_CONFIG = './config.json'
LOG_PATH = './service.log'

initLogger(LOG_PATH)

def create_app():
    """ Function that initialises the application from the config. """
    _app = Flask(__name__)

    # TODO: load config from file : _app.config.from_json(CONFIG)
    _app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'

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

    # Interesting read if you want multiple databases
    # https://stackoverflow.com/questions/36877914/flask-sqlalchemy-on-the-fly-connections-to-multiple-databases
    db = SQLAlchemy(app)

    test_app = Service(db)
    app.register_blueprint(test_app.get_api(), url_prefix='/v1')
    app.run(host="0.0.0.0", port=5000)
