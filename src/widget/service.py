from typing import Dict
from flask import Blueprint
from .controller import WidgetController
from .singleton import Singleton
from .repo import WidgetRepo
from .api import Api


class WidgetService(object, metaclass=Singleton):
    """ The WidgetService acts like a factory to create the WidgetController
    and the associated API.
    """
    def __init__(self, config: Dict):
        self._repo = WidgetRepo(config)
        self._controller = WidgetController(self._repo)
        Api.controller = self._controller

    def get_controller(self) -> WidgetController:
        return self._controller

    def get_api(self) -> Blueprint:
        return Api.v1_blueprint
