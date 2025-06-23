# agents.py
class Agent:
    def __init__(self, name=None, instructions=None):
        self.name = name
        self.instructions = instructions

    def run(self, *args, **kwargs):
        ...

class Runner:
    def __init__(self, agent):
        self.agent = agent

    def run(self, *args, **kwargs):
        return self.agent.run(*args, **kwargs)
    