import json
from test_app.api import Api


class Controller(object):
  _widget_list = [
      'widget1',
      'widget2',
      'widget3',
    ]
  def __init__(self, db):
    self._db = db
    Api.controller = self

  def get_api(self):
    return Api.v1_blueprint

  def get_widgets(self):
    return self._widget_list

  def create_widget(self, data):
    print(f"Data: {data}")
    new_object = json.loads(data)
    self._widget_list.append(new_object["name"])
        
