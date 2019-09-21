import json

class WidgetController(object):
    """ The WidgetController contains just the business-logic. 
    It has no notion of the Api or the fact its being hosted as a service.
    """
    _widget_list = [
        'widget1',
        'widget2',
        'widget3',
    ]

    def __init__(self, db):
      self._db = db

    def get_widgets(self):
      return self._widget_list

    def create_widget(self, data):
      new_object = json.loads(data)
      self._widget_list.append(new_object["name"])
      return new_object["name"]
        
