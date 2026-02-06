from .policy_base import BasePolicy


class RandomPolicy(BasePolicy):
    def __init__(self):
        super().__init__()

    def choose_actions(self, observation: list):
        """
        Choose a random action for each agent.

        Args:
            observation (list): The observation for each agent.

        Returns:
            dict: The random action for each agent.
        """
        return {n: self.env.action_space(n).sample() for n in self.env.agents}
