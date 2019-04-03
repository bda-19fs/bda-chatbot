def correct(token, grammar):
    return grammar[token] if token in grammar.keys() else token

def correct_tokens(tokens, grammar):
    return [correct(token, grammar) for token in tokens]

def correct_doc(token_doc, grammar):
    return list(map(lambda t: correct_tokens(t, grammar), token_doc))
