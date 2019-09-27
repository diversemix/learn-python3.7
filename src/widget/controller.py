from .dto import WidgetDto


class WidgetController(object):
    """ The WidgetController contains just the business-logic.
    It has no notion of the Api or the fact its being hosted as a service.
    """
    def __init__(self, repo):
        self._repo = repo
        n_widgets = len(self.get_all_widgets())
        if (n_widgets == 0):
            self.create_widget()
            self.get_all_widgets()

    def get_all_widgets(self):
        return self._repo.get_all_widgets()

    def create_widget(self, dto=None):
        if (dto is None):
            dto = WidgetDto(name='paper clip', weight_kg=0.005)

        self._repo.add_widget(dto)
