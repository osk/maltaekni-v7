from levenshtein import ld_recusive, ld_wf

test_cases = [
    ("empty", "", "", 0),
    ("not string", True, False, 0),
    ("single", "a", "", 1),
    ("single", "", "a", 1),
    ("one diff", "bb", "ba", 1),
    ("two different strings", "bbbb", "aaaa", 4),
    ("long string one diff", "asdfasdfasdf", "asdfasxfasdf", 1),
    ("long string vs single char", "qwertyuiop", "xx", 10),
]


def test_levenshtein_distance_recursive():
    for case in test_cases:
        assert ld_recusive(case[1], case[2]) == case[3], case[0]


def test_levenshtein_distance_wf():
    for case in test_cases:
        assert ld_wf(case[1], case[2]) == case[3], case[0]


def test_levenshtein_distance_wf_long():
    assert ld_wf("hello world", "and now for something completely different") == 36
