from ..widget.service import WidgetService

# Expect DeprecationWarning, see
# https://github.com/pallets/jinja/issues/969

def test_service_has_controller(mocker):
    config = mocker.Mock()
    widget_service = WidgetService(config)
    assert widget_service.get_controller() is not None

def test_service_has_api(mocker):
    config = mocker.Mock()
    widget_service = WidgetService(config)
    assert widget_service.get_api() is not None
