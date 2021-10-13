from cars import __version__
from cars.cars import Vehicle


def test_version():
    assert __version__ == "0.1.0"


def test_vehicle():
    assert Vehicle('white')
