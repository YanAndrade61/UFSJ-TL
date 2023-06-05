import yaml
from automaton import automaton

if __name__ == '__main__':
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    x = automaton(config)
    print(x.start)
    print(x.ends)
    print(x.rules)
