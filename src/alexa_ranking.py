def get_top_n_alexa_domains(top_n, path='data/alexa-top-10000.txt'):
    with open(path, 'r') as f:
        return f.read().split('\n')[:top_n]
