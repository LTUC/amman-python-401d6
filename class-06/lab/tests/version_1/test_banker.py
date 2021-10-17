import pytest
from game_of_greed.banker import Banker

pytestmark = [pytest.mark.version_1, pytest.mark.version_2]


def test_new_banker():
    banker = Banker()
    assert banker.balance == 0
    assert banker.shelved == 0


def test_shelf():
    banker = Banker()
    banker.shelf(100)
    assert banker.shelved == 100
    assert banker.balance == 0


def test_deposit():
    banker = Banker()
    banker.shelf(100)
    banker.bank()
    assert banker.shelved == 0
    assert banker.balance == 100


def test_clear_shelf():
    banker = Banker()
    banker.shelf(100)
    banker.bank()
    banker.shelf(50)
    banker.clear_shelf()
    assert banker.balance == 100
    assert banker.shelved == 0
