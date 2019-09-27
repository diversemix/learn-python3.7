import pytest
from ..widget.service import WidgetService

# Expect DeprecationWarning, see
# https://github.com/pallets/jinja/issues/969

@pytest.fixture
def config(tmpdir):
  return { "database_uri" : tmpdir + "/tmp.sqlite3"}

def test_service_has_controller(config):
    widget_service = WidgetService(config)
    assert widget_service.get_controller() is not None

def test_service_has_api(config):
    widget_service = WidgetService(config)
    assert widget_service.get_api() is not None
