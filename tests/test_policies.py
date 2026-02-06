import pytest


def test_random_policy(policy_random_levers_fixture):
    """
    Test that the RandomPolicy class can generate data for the Levers environment.
    """
    episode = policy_random_levers_fixture.generate_episode()
    print(episode)
    assert len(episode) == 2