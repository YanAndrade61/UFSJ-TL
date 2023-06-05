class automaton:
    def __init__(self, config: dict):
        self.start = config['start']
        self.ends = set(config['ends'])
        self.rules = config['rules']
