class Scorer:
    def __init__(self, scoresheet):
        self._scoresheet = scoresheet

    def calculate_scores(self):
        return {tla: data['flags'] for tla, data in self._scoresheet.items()}

