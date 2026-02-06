from copy import copy

class BasePolicy:
    def __init__(self):
        pass
    
    def choose_actions(self, observation: list):
        raise NotImplementedError()

    def generate_episode(self):
        """
        Generate a single episode.

        Returns:
            list: The generated episode.
        """
        # initialize lists to store generated data
        observations = []
        actions = []
        rewards = []
        terminations = []
        truncations = []
        
        o, _ = self.env.reset() # reset the environment
        agents = copy(self.env.possible_agents) # remember agents

        # loop until all agents have terminated
        while self.env.agents:
            observations.append(o) # add observations to its list

            # generate actions for all agents
            a = self.choose_actions(o)
            
            # observations, rewards, terminations, truncations, infos
            o, r, d, t, i = self.env.step(a) 

            # add actions, rewards, terminations, and truncations to their lists
            actions.append(a)
            rewards.append(r)
            terminations.append(d)
            truncations.append(t)

        # separate data across agents
        episode = []
        for n in agents:
            # separate data for agent n and add it to the episode
            episode.append([[
                observations[t][n], 
                actions[t][n], 
                rewards[t][n], 
                terminations[t][n], 
                truncations[t][n]
            ] for t in range(len(observations))])
        
        return episode
    
    def generate_dataset(self):
        self.generate_episode()
        raise NotImplementedError()
