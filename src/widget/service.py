from .singleton import Singleton

class WidgetService(object, metaclass=Singleton):
    """ The WidgetService acts like a factory to create the WidgetController
    and the associated API.
    """
    def __init__(self, db):
      self._controller = WidgetController(db)
      Api.controller = self._controller

    def get_controller(self):
      return self._controller

    def get_api(self):
      return Api.v1_blueprint
