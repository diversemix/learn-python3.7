from .controller import WidgetController
from .singleton import Singleton
from .repo import WidgetRepo
from .api import Api

class WidgetService(object, metaclass=Singleton):
    """ The WidgetService acts like a factory to create the WidgetController
    and the associated API.
    """
    def __init__(self, config):
      self._repo = WidgetRepo(config)
      self._controller = WidgetController(self._repo)
      Api.controller = self._controller

    def get_controller(self):
      return self._controller

    def get_api(self):
      return Api.v1_blueprint
