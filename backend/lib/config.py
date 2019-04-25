def ui_config():
    dataset = [
        'Stackexchange',
        'Ionesoft'
    ]
    algorithm = [
        'Plain',
        'Stemming',
        'Lemmatization',
        'Stopwords',
        'Stopwords & stemming',
        'Stopwords & lemmatization'
    ]
    domain_limit = [
        ' 0%  - 100%',
        ' 5%  -  95%',
        '10%  -  90%'
    ]
    return dataset, algorithm, domain_limit
