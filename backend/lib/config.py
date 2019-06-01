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
        'max_df 100%',
        'max_df  75%',
        'max_df  50%'
    ]
    return dataset, algorithm, domain_limit
