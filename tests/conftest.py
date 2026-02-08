import pytest

from deepfabm.models.model_rwalksb import RandomWalkWithStructuralBreak


@pytest.fixture(scope="class")
def model_rwalksb_fixture():
    return RandomWalkWithStructuralBreak()
