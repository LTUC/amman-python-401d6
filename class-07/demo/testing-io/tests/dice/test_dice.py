from tests.dice.dice_simulator import diff
from testing_io.dice import play_dice


def test_quitter():
    diffs = diff(play_dice, path="tests/dice/quitter.sim.txt")
    assert not diffs, diffs


def test_seven_then_quit():
    diffs = diff(play_dice, path="tests/dice/seven_then_quit.sim.txt")
    assert not diffs, diffs
