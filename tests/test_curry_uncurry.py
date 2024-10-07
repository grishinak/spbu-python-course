import pytest
from project.curry_uncurry import curry_explicit, uncurry_explicit


@pytest.mark.parametrize(
    "function, arity, args, expected_exception",
    [
        (lambda x: f"<{x}>", 0, (1,), TypeError),  
        (lambda x: f"<{x}>", 1, (1, 3), TypeError),  # Too many arguments
        (lambda x: f"<{x}>", -1, (1,), ValueError),  # Negative arity
    ],
)
def test_curry_exceptions(function, arity, args, expected_exception):
    with pytest.raises(expected_exception):
        curry_explicit(function, arity)(*args)


@pytest.mark.parametrize(
    "function, arity, args, expected_output",
    [
        (lambda: f"<>", 0, (), "<>"),  # zero arity
        (lambda x: f"<{x}>", 1, (1,), "<1>"),  # one arity
        (print, 2, (1, 2), None),  #
    ],
)
def test_curry_success(function, arity, args, expected_output):
    result = curry_explicit(function, arity)(*args)
    if expected_output is None:
        assert result is None
    else:
        assert result == expected_output


@pytest.mark.parametrize(
    "function, arity, args, expected_output",
    [
        (lambda x, y, z: f"<{x},{y},{z}>", 3, (123, 456, 562), "<123,456,562>"),
    ],
)
def test_curry_uncurry_example(function, arity, args, expected_output):
    f2 = curry_explicit(function, arity)
    g2 = uncurry_explicit(f2, arity)
    assert f2(*args) == expected_output
    assert g2(*args) == expected_output


# TODO: more tests for uncurry
