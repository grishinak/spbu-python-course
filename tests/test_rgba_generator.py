import pytest
from project.rgba_generator import get_rgba_element


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, (0, 0, 0, 0)),
        (1, (0, 0, 0, 2)),
        (50, (0, 0, 0, 100)),
        (51, (0, 0, 1, 0)),
        (256 * 51, (0, 1, 0, 0)),
        (256 * 256 * 51, (1, 0, 0, 0)),
        # (256*256*256*51, (255,255,255,0)),    #TODO:need to optimize for big indexes
        # (256*256*256*51+1, (255,255,255,2)),
    ],
)
def test_get_rgba_element(index, expected):
    """A test to check for an excpected result when the index is in range."""
    assert get_rgba_element(index) == expected


@pytest.mark.parametrize(
    "index",
    [
        -1,  # negative index
        256 * 256 * 256 * 51,  # out of range
    ],
)
def test_get_rgba_element_index_error(index):
    """A test to check for an IndexError exception when the index is out of range."""
    with pytest.raises(IndexError):
        get_rgba_element(index)
