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
        # (256 * 256 * 256 * 50, (255, 255, 255, 100)),  # Last element (255, 255, 255, 100) #TODO: need to optimize
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


# @pytest.mark.parametrize(
#     "index, expected",
#     [
#         (0, (0, 0, 0, 0)),
#         (1, (0, 0, 0, 2)),
#         (50, (0, 0, 0, 100)),
#         (51, (0, 0, 1, 0)),
#         (256 * 51, (0, 1, 0, 0)),
#         (256 * 256 * 51, (1, 0, 0, 0)),
#     ],
# )
# def test_get_rgba_element(index, expected):
#     """A test to check for an excpected result when the index is in range."""
#     assert get_rgba_element(index) == expected


# @pytest.mark.parametrize(
#     "index",
#     [
#         -1,  # negative index
#         256 * 256 * 256 * 51,  # out of range
#     ],
# )
# def test_get_rgba_element_index_error(index):
#     """A test to check for an IndexError exception when the index is out of range."""
#     with pytest.raises(IndexError):
#         get_rgba_element(index)
