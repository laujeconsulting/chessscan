class TCM:
    """
    Table of Correct Moves (TCM) class to track suspicious moves and their corresponding
    correct moves with frequency counts.
    """

    def __init__(self):
        # Initialize the frequency table as a dictionary
        self.frequency_table = {}

    def increment_frequency(self, suspicious_move: str, correct_move: str) -> None:
        """
        Increment the frequency of a correct move for a given suspicious move.

        :param suspicious_move: The suspicious chess move.
        :param correct_move: The correct chess move for the suspicious move.
        :raises ValueError: If the suspicious move does not exist or if the correct move
            does not exist.
        """
        if suspicious_move not in self.frequency_table:
            raise ValueError(f"Suspicious move '{suspicious_move}' does not exist.")

        if correct_move not in self.frequency_table[suspicious_move]:
            raise ValueError(
                f"Correct move '{correct_move}' does not exist for suspicious move '{suspicious_move}'."
            )

        # Increment the frequency
        self.frequency_table[suspicious_move][correct_move] += 1

    def get_correct_moves(self, suspicious_move: str) -> dict:
        """
        Get the list of correct moves and their frequencies for a given suspicious move.

        :param suspicious_move: The suspicious chess move.
        :return: A dictionary of correct moves and their frequencies, or None if the
            suspicious move does not exist.
        """
        return self.frequency_table.get(suspicious_move, None)

    def add_suspicious_move(self, suspicious_move: str) -> None:
        """
        Add a new suspicious move to the frequency table with an empty dictionary.

        :param suspicious_move: The suspicious chess move.
        """
        if suspicious_move not in self.frequency_table:
            self.frequency_table[suspicious_move] = {}

    def add_correct_move(self, suspicious_move: str, correct_move: str) -> None:
        """
        Add a new correct move for a specific suspicious move with initial frequency.

        :param suspicious_move: The suspicious chess move.
        :param correct_move: The correct chess move to be added.
        """
        if suspicious_move not in self.frequency_table:
            raise ValueError(
                f"Suspicious move '{suspicious_move}' does not exist. Please add it first."
            )

        if correct_move not in self.frequency_table[suspicious_move]:
            self.frequency_table[suspicious_move][correct_move] = 0
