import yaml
from automaton import automaton

if __name__ == '__main__':
    with open("examples/config2.yaml", "r") as f:
        config = yaml.safe_load(f)
    x = automaton(config)
    palavras = ['abab','abbaa','b','aaaa','abba']
    for s in palavras:
        x.process(s)
