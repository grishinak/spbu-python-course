import pytest
from project.rgba_generator import (get_rgba_element)


@pytest.mark.parametrize("index, expected", [
    (0, (0,0,0,0)),
    (1, (0,0,0,2)),
    (50, (0,0,1,0)),
    (256*50, (0,1,0,0)),
    (256*256*50, (1,0,0,0)),
    # (256*256*256*50, (255,255,255,0)),
    # (256*256*256*50+1, (255,255,255,2)),
])
def test_get_rgba_element(index, expected):
    assert get_rgba_element(index) == expected