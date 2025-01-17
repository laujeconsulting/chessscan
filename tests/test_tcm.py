from heuristics.move_corrector.tcm import TCM
import pytest


@pytest.fixture
def tcm():
    """
    Fixture for creating a new TCM instance for each test.
    """
    return TCM()


def test_add_suspicious_move(tcm):
    """
    Test adding a new suspicious move.
    """
    tcm.add_suspicious_move("e4")
    assert "e4" in tcm.frequency_table


def test_add_correct_move(tcm):
    """
    Test adding a correct move for a suspicious move.
    """
    tcm.add_suspicious_move("e2e4")
    tcm.add_correct_move("e2e4", "e4")
    assert "e4" in tcm.frequency_table["e2e4"]


def test_increment_frequency(tcm):
    """
    Test incrementing frequency of a correct move.
    """
    tcm.add_suspicious_move("e2e4")
    tcm.add_correct_move("e2e4", "e4")
    tcm.increment_frequency("e2e4", "e4")
    assert tcm.frequency_table["e2e4"]["e4"] == 1


def test_increment_frequency_nonexistent_suspicious_move(tcm):
    """
    Test incrementing frequency for a nonexistent suspicious move.
    """
    with pytest.raises(ValueError, match="Suspicious move 'e2e5' does not exist."):
        tcm.increment_frequency("e2e5", "e4")


def test_increment_frequency_nonexistent_correct_move(tcm):
    """
    Test incrementing frequency for a nonexistent correct move.
    """
    tcm.add_suspicious_move("e2e4")
    with pytest.raises(
        ValueError, match="Correct move 'e5' does not exist for suspicious move 'e2e4'."
    ):
        tcm.increment_frequency("e2e4", "e5")


def test_get_correct_moves(tcm):
    """
    Test retrieving correct moves for a suspicious move.
    """
    tcm.add_suspicious_move("e2e4")
    tcm.add_correct_move("e2e4", "e4")
    tcm.increment_frequency("e2e4", "e4")
    correct_moves = tcm.get_correct_moves("e2e4")
    assert correct_moves == {"e4": 1}


def test_get_correct_moves_nonexistent(tcm):
    """
    Test getting correct moves for a nonexistent suspicious move.
    """
    result = tcm.get_correct_moves("e2e5")
    assert result is None


def test_increment_same_correct_move_multiple_times(tcm):
    """
    Test incrementing the same correct move multiple times.
    """
    tcm.add_suspicious_move("e2e4")
    tcm.add_correct_move("e2e4", "e4")
    for _ in range(5):
        tcm.increment_frequency("e2e4", "e4")
    assert tcm.frequency_table["e2e4"]["e4"] == 5


def test_adding_multiple_correct_moves(tcm):
    """
    Test adding multiple correct moves for the same suspicious move.
    """
    tcm.add_suspicious_move("e2e4")
    tcm.add_correct_move("e2e4", "e4")
    tcm.add_correct_move("e2e4", "e5")

    tcm.increment_frequency("e2e4", "e4")
    tcm.increment_frequency("e2e4", "e5")

    assert tcm.frequency_table["e2e4"]["e4"] == 1
    assert tcm.frequency_table["e2e4"]["e5"] == 1


def test_nonexistent_suspicious_move_add_correct_move(tcm):
    """
    Test adding a correct move to a nonexistent suspicious move.
    """
    with pytest.raises(
        ValueError, match="Suspicious move 'e2e4' does not exist. Please add it first."
    ):
        tcm.add_correct_move("e2e4", "e5")
