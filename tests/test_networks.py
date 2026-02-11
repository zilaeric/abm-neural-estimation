import pytest

from deepfabm.networks import Network, load_network


def test_load_network_unknown_raises_value_error():
    with pytest.raises(ValueError):
        load_network("does-not-exist")


def test_load_network_returns_network_instance():
    network = load_network("lstm")
    assert isinstance(network, Network)
