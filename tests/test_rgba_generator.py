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
    ],
)
def test_get_rgba_element_valid(index, expected):
    """Test valid indices to ensure correct RGBA vector is returned."""
    assert get_rgba_element(index) == expected


@pytest.mark.parametrize("invalid_index", [-1, 256 * 256 * 256 * 51])
def test_get_rgba_element_invalid(invalid_index):
    """Test invalid indices to ensure IndexError is raised."""
    with pytest.raises(IndexError):
        get_rgba_element(invalid_index)
