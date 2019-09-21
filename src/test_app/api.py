#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This file contains endpoints for the service.
"""
import logging
from flask import Blueprint
from flask import current_app
from flask import request
from flask import jsonify
from test_app.singleton import Singleton


HTTP_200_OK = 200
HTTP_400_BAD_REQUEST = 400


class Api(object, metaclass=Singleton):
    v1_blueprint = Blueprint('v1', 'v1_blueprint') # Create a versioned API
    controller = None
    def __init__(self, controller):
        self.controller = controller
        
    @staticmethod
    @v1_blueprint.route('/widgets', methods=['GET'])
    def get_widgets():
        try:
            widgets = Api.controller.get_widgets()
        except ValueError as e:
            return jsonify(error=str(e)), HTTP_400_BAD_REQUEST

        return jsonify(widgets=widgets), HTTP_200_OK

    @staticmethod
    @v1_blueprint.route('/widgets', methods=['POST'])
    def put_widget():
        if not request.data:
            msg = "No data in request"
            logging.error(msg)
            return jsonify(error=msg), HTTP_400_BAD_REQUEST

        data = request.data.decode('ascii')

        widget = None
        try:
            Api.controller.create_widget(data)
        except ValueError as e:
            return jsonify(error=str(e)), HTTP_400_BAD_REQUEST

        return jsonify(widget=widget), HTTP_200_OK
