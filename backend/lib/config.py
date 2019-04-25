def ui_config():
    dataset = [
        'Ionesoft',
        'Stackexchange'
    ]
    algorithm = [
        'TF-IDF',
        'TF-IDF with stemming',
        'TF-IDF with lemming'
    ]
    domain_limit = [
        '0% - 100%',
        '15% - 85%',
        '25% - 75%'
    ]
    return dataset, algorithm, domain_limit
