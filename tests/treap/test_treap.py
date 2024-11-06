import pytest
from collections.abc import MutableMapping
from project.treap.treap import Treap

@pytest.fixture
def sample_treap():
    """Creates a test treap with some elements."""
    treap = Treap()
    treap[10] = "A"
    treap[20] = "B"
    treap[5] = "C"
    treap[15] = "D"
    return treap

@pytest.mark.parametrize("key,value", [
    (10, "A"),
    (20, "B"),
    (5, "C"),
    (15, "D"),
])
def test_getitem(sample_treap, key, value):
    """Tests retrieving an element by key."""
    assert sample_treap[key] == value

@pytest.mark.parametrize("key,value", [
    (25, "E"),
    (30, "F"),
    (1, "G"),
])
def test_setitem(sample_treap, key, value):
    """Tests adding a new element."""
    sample_treap[key] = value
    assert sample_treap[key] == value

@pytest.mark.parametrize("key", [10, 20, 5, 15])
def test_contains(sample_treap, key):
    """Tests whether the key exists in the treap."""
    assert key in sample_treap

@pytest.mark.parametrize("key", [100, 200, -5])
def test_not_contains(sample_treap, key):
    """Tests whether the key does not exist in the treap."""
    assert key not in sample_treap

@pytest.mark.parametrize("key", [10, 20, 5, 15])
def test_delitem(sample_treap, key):
    """Tests deleting an element from the treap."""
    del sample_treap[key]
    assert key not in sample_treap

def test_len(sample_treap):
    """Tests the length of the treap."""
    assert len(sample_treap) == 4
    sample_treap[25] = "E"
    assert len(sample_treap) == 5
    del sample_treap[10]
    assert len(sample_treap) == 4

def test_iteration(sample_treap):
    """Tests forward traversal (in-order traversal) of the treap."""
    keys = list(sample_treap)
    assert keys == [5, 10, 15, 20]

def test_reverse_iteration(sample_treap):
    """Tests reverse traversal (reverse in-order traversal) of the treap."""
    keys = list(reversed(sample_treap))
    assert keys == [20, 15, 10, 5]

def test_key_error_getitem(sample_treap):
    """Tests KeyError when trying to access a non-existing element."""
    with pytest.raises(KeyError):
        _ = sample_treap[100]

def test_key_error_delitem(sample_treap):
    """Tests KeyError when trying to delete a non-existing element."""
    with pytest.raises(KeyError):
        del sample_treap[100]

# tests for the task requirements

def test_iterable(sample_treap):
    """Tests that the treap is iterable, returning keys in correct order."""
    # check that iterating over the treap returns keys in ascending order
    assert list(sample_treap) == [5, 10, 15, 20]

def test_reverse_iterable(sample_treap):
    """Tests that the treap can be iterated in reverse order."""
    # check that reverse iteration works as expected
    assert list(reversed(sample_treap)) == [20, 15, 10, 5]

def test_mutable_mapping(sample_treap):
    """Tests that the treap is a valid MutableMapping."""
    # verify that Treap behaves like a MutableMapping
    assert isinstance(sample_treap, MutableMapping)

def test_access_through_brackets(sample_treap):
    """Tests accessing elements using the bracket notation."""
    assert sample_treap[10] == "A"
    sample_treap[10] = "Updated"
    assert sample_treap[10] == "Updated"

def test_delete_through_brackets(sample_treap):
    """Tests deleting elements using the bracket notation."""
    del sample_treap[10]
    with pytest.raises(KeyError):
        _ = sample_treap[10]

def test_in_operator(sample_treap):
    """Tests the use of the 'in' operator to check key existence."""
    assert 5 in sample_treap
    assert 100 not in sample_treap

@pytest.mark.parametrize("key,value", [
    (10, "A"),
    (5, "B"),
])
def test_insert_new_elements(sample_treap, key, value):
    """Tests inserting new elements into the treap."""
    sample_treap[key] = value
    assert sample_treap[key] == value

@pytest.mark.parametrize("key", [10, 5, 15, 20])
def test_remove_existing_elements(sample_treap, key):
    """Tests removing elements from the treap."""
    del sample_treap[key]
    assert key not in sample_treap
