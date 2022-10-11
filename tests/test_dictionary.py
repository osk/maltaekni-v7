from dictionary import Dictionary
from pytest import raises


def test_dictionary_empty():
    d = Dictionary([])
    assert not d.has("foo")


def test_dictionary_single():
    d = Dictionary(["FOO"])
    assert d.has("foo")
    assert not d.has("bar")


def test_raises_if_not_list():
    with raises(Exception):
        Dictionary(None)


def test_raises_if_list_with_non_string():
    with raises(Exception):
        Dictionary([None])


def test_has_sentence():
    d = Dictionary(["foo", "bar"])
    assert d.sentence("foo, bar!") == [("foo", True), ("bar", True)]
