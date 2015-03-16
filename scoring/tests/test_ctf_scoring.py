
# Path hackery
import os.path
import sys
ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, ROOT)

from score import Scorer, InvalidScoresheetException

def test_scores():
    input_data = {
        'ABC': {'flags': 0},
        'DEF': {'flags': 1},
        'GHI': {'flags': 2}
    }
    expected = {
        'ABC': 0,
        'DEF': 1,
        'GHI': 2
    }

    scorer = Scorer(input_data)
    scores = scorer.calculate_scores()

    assert expected == scores, "Wrong scores!"

def test_negative_score():
    input_data = {
        'ABC': {'flags': -1},
        'DEF': {'flags': 1},
        'GHI': {'flags': 2}
    }

    try:
        scorer = Scorer(input_data)
        scores = scorer.calculate_scores()
    except InvalidScoresheetException:
        pass
    else:
        assert False, "Should error when scores are invalid"

def test_float_score():
    input_data = {
        'ABC': {'flags': 1.5},
        'DEF': {'flags': 1},
        'GHI': {'flags': 2}
    }

    try:
        scorer = Scorer(input_data)
        scores = scorer.calculate_scores()
    except InvalidScoresheetException:
        pass
    else:
        assert False, "Should error when scores are invalid"

def test_string_score():
    input_data = {
        'ABC': {'flags': "1"},
        'DEF': {'flags': 1},
        'GHI': {'flags': 2}
    }

    try:
        scorer = Scorer(input_data)
        scores = scorer.calculate_scores()
    except InvalidScoresheetException:
        pass
    else:
        assert False, "Should error when scores are invalid"

def test_bad_scores_validation():
    input_data = {
        'ABC': {'flags': -1},
        'DEF': {'flags': 1},
        'GHI': {'flags': 2}
    }

    try:
        scorer = Scorer(input_data)
        scores = scorer.calculate_scores()
    except InvalidScoresheetException:
        pass
    else:
        assert False, "Should error when scores are invalid"

def test_bad_unclaimed_validation():
    input_data = {
        'ABC': {'flags': 4},
        'DEF': {'flags': 1},
        'GHI': {'flags': 2}
    }
    extra = {'unclaimed_flags': -3}

    try:
        scorer = Scorer(input_data)
        scores = scorer.validate(extra)
    except InvalidScoresheetException:
        pass
    else:
        assert False, "Should error when scores are invalid"

def test_validation_too_many_flags():
    input_data = {
        'ABC': {'flags': 0},
        'DEF': {'flags': 1},
        'GHI': {'flags': 2}
    }
    extra = {'unclaimed_flags': 42}
    expected = {
        'ABC': 0,
        'DEF': 1,
        'GHI': 2
    }

    try:
        scorer = Scorer(input_data)
        scores = scorer.validate(extra)
    except InvalidScoresheetException:
        pass
    else:
        assert False, "Should error when scores are invalid"

