class Automaton:
    def __init__(self, config: dict):
        self.start = config['start']
        self.ends = set(config['ends'])
        self.rules = config['rules']
    
    def process(self, string: str):
        
        states_on = set([self.start])
        
        for symbol in string:

            #Update the active states
            states = set()
            for s in states_on:
                states |= self.next_state(s,symbol)
                               
            states_on = states

        return len(states_on & self.ends) > 0
        
    def process_step_by_step(self, string: str):
        
        states_on = set([self.start])
        all_states = []
        all_states.append(states_on)

        for symbol in string:

            #Update the active states
            states = set()
            for s in states_on:
                states |= self.next_state(s,symbol)
                               
            states_on = states
            all_states.append(states_on)

        return len(states_on & self.ends) > 0, all_states

    def next_state(self,state: str, symbol: str):
        return set(self.rules[state].get(symbol,[]))
