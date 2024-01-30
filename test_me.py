import pytest

@pytest.mark.good
def test_one():
    assert 1 == 1

@pytest.mark.bad
def test_two():
    assert 1 == 2