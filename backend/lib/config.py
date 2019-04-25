def ui_config():
    dataset = [
        'Stackexchange',
        'Ionesoft'
    ]
    algorithm = [
        'TF-IDF',
        'TF-IDF with stemming',
        'TF-IDF with lemmatization',
        'TF-IDF stopwords',
        'TF-IDF stopwords stemming',
        'TF-IDF stopwords lemmatization',
        'SKIP-GRAM',
        'SKIP-GRAM with stemming',
        'SKIP-GRAM with lemmatization',
        'SKIP-GRAM stopwords',
        'SKIP-GRAM stopwords stemming',
        'SKIP-GRAM stopwords lemmatization'
    ]
    domain_limit = [
        ' 0%  - 100%',
        ' 5%  -  95%',
        '10%  -  90%'
    ]
    return dataset, algorithm, domain_limit
