import pytest

from deepfabm.models import Model, load_model


def test_load_model_unknown_raises_value_error():
    with pytest.raises(ValueError):
        load_model("does-not-exist")


def test_load_model_returns_model_instance():
    model = load_model("rwalksb")
    assert isinstance(model, Model)
