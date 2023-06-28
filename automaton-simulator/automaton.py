class Automaton:
    def __init__(self, config: dict):
        self.type = config['type']
        self.start = config['start']
        self.ends = set(config['ends'])
        self.rules = config['rules']
    
    def process(self, string: str):
        
        states_on = set([self.start])
        states_on |= self.next_state(self.start,"vz")
                
        for symbol in string:

            #Update the active states
            states = set()
            for s in states_on:
                states |= self.next_state(s,symbol)
                states |= self.next_state(s,"vz")
                               
            states_on = states

        return len(states_on & self.ends) > 0
    
    def process_stack(self, string: str):
        stacks_old = {("vz",): [self.start]}
        self.void_rule()
                
        for symbol in string:
            stacks_now = {}
            print("Letra:", symbol)

            for stack, states in stacks_old.items():
                print("\tPilha:", stack)
                for state in states:
                    print("\tEstado:", state)
                    self.next_state_stack(state=state, symbol=symbol, stack=stack, stacks_now=stacks_now)
                    
            stacks_old = stacks_now
            print(stacks_old)

        print("acabou a palavra")

        for stack, states in stacks_old.items():
            for state in states:
                return self.end_state(state=state, stack=stack)
            
        return 0
        return len(states_on & self.ends) > 0
        
    def process_step_by_step(self, string: str):
        
        states_on = set([self.start])
        states_on |= self.next_state(self.start,"vz")

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
    
    def next_state_stack(self,state: str, symbol: str, stack: str, stacks_now: dict):
        states_rules = self.rules[state]
        for rule in states_rules:
            #print(rule)
            if rule[0] != symbol: continue
            if stack[-1] != rule[1] and rule[1] != 'vz': continue
            
            if rule[1] == 'vz':
                stack_nex = list(stack)
            else:
                stack_nex = list(stack[:-1])
            if len(stack_nex) == 0: stack_nex.append("vz")
            if(rule[2] != "vz"):
                stack_nex = stack_nex + [c for c in rule[2]]
            
            for state_nex in rule[3]:
                stacks_now.setdefault(tuple(stack_nex), []).append(state_nex)
                self.void_rule()

    def end_state(self,state: str, stack: str):
        states_rules = self.rules[state]
        for rule in states_rules:
            if rule[0] != 'INTE' or stack[-1] != "vz": continue
            
            for state_on in rule[3]:
                if state_on in self.ends: 
                    return 1
        
        return 0

    #def void_rule(self,state: str, symbol: str, stack: str, stacks_now: dict):
    def void_rule(self):
        print("", end="")
