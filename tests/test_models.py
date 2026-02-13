import numpy as np
import pytest

from deepfabm.models import Model, load_model


def test_load_model_unknown_raises_value_error():
    with pytest.raises(ValueError):
        load_model("does-not-exist")


def test_load_model_returns_model_instance():
    model = load_model("rwalksb")
    assert isinstance(model, Model)


def test_rwalkd_replicability():
    np.random.seed(42)
    model = load_model("rwalkd")
    returns = model.generate({"d": 0.6}, 5, 5, 1)
    expected = np.array(
        [[0.0668132, 0.32567142, 0.16077073, 0.01407643, 0.11542942]],
        dtype=np.float64,
    )
    np.testing.assert_allclose(returns, expected, rtol=1e-5)
