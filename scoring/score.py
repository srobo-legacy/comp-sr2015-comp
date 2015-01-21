class Scorer:
    def __init__(self, scoresheet):
        self._scoresheet = scoresheet

    def calculate_scores(self):
        return {tla: len(data['flags']) for tla, data in self._scoresheet.items()}

