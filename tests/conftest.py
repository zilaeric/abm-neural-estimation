import pytest

from deepfabm.policies.policy_random import RandomPolicy


@pytest.fixture(scope="class")
def policy_random_levers_fixture():
    return RandomPolicy()
