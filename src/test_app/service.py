from test_app.controller import Controller
from test_app.singleton import Singleton


class Service(object, metaclass=Singleton):

    def __init__(self, db):
      self._controller = Controller(db)

    def get_controller(self):
      return self._controller

    def get_api(self):
      return self._controller.get_api()
