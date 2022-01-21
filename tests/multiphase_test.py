from pollination.honeybee_radiance.multiphase import ViewMatrix
from pollination.honeybee_radiance.multiphase import DaylightMatrix
from queenbee.plugin.function import Function


def test_view_mtx():
    function = ViewMatrix().queenbee
    assert function.name == 'view-matrix'
    assert isinstance(function, Function)


def test_daylight_mtx():
    function = DaylightMatrix().queenbee
    assert function.name == 'daylight-matrix'
    assert isinstance(function, Function)
