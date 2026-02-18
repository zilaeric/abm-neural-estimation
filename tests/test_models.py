import numpy as np
import pytest

from deepfabm.models import Model, list_models, load_model


def test_load_model_unknown_raises_value_error():
    with pytest.raises(ValueError):
        load_model("does-not-exist")


def test_load_model_returns_model_instance():
    # Ensure every registered model can be instantiated
    for model_name in list_models():
        model = load_model(model_name)
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


def test_every_model_has_default_parametrization():
    # Ensure every registered model has the "default" parametrization defined
    for model_name in list_models():
        model = load_model(model_name)
        assert "default" in model.list_parametrizations(), (
            f"Model '{model_name}' must define a 'default' parametrization. "
            f"Available: {model.list_parametrizations()}."
        )
        assert isinstance(model.get_parameters("default"), dict)
