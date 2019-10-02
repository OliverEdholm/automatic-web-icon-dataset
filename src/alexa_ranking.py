def get_top_n_alexa_domains(top_n, path='data/alexa-top-10000.txt'):
    with open(path, 'r') as f:
        all_domains = f.read().split('\n')[:top_n]

    all_extension_agnostics = set()

    single_extension_domains = []
    for domain in all_domains:
        extension_agnostic = domain.split('.')[0]

        if extension_agnostic not in all_extension_agnostics:
            all_extension_agnostics.add(extension_agnostic)

            single_extension_domains.append(domain)

    return single_extension_domains
