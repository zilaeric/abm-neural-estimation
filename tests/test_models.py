import pytest


def test_model(model_rwalksb_fixture):
    """
    Test that the RandomWalkStructuralBreak class can generate data.
    """
    model = model_rwalksb_fixture()
    assert model is not None