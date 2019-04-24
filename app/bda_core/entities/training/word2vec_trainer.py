import gensim
import numpy as np


class Config:
    '''
    This class represents the configuration for the Word2Vec model.
    '''
    def __init__(self, dimension=150, window_size=5, workers=3, use_skip_gram=1, epochs=10):
        self.dimension = dimension
        self.window_size = window_size
        self.workers = workers
        self.use_skip_gram = use_skip_gram
        self.epochs = epochs


def fit_model(sentences, config):
    '''
    Fits the Word2Vec model with the given sentences. The vectors were normalized after the training.
    A further training of the model is not possible.
    :param sentences: A python list of sentences
    :param config: The config for the model
    :return: The trained Word2Vec model
    '''
    model = gensim.models.Word2Vec(size=config.dimension, window=config.window_size, workers=config.workers,
                                   sg=config.use_skip_gram)
    model.build_vocab(sentences)
    model.train(sentences, total_examples=len(sentences), epochs=config.epochs)
    model.init_sims(replace=True)
    return model


def avg_word_vector(model, word_list):
    '''
    Calculates the average vector of a list of words. The average vector is the mean
    of all word vectors. Only words of the Word2Vec vocabulary can be considered.
    :param model: The trained Word2Vec model
    :param word_list: A python list of words
    :return: The average vector
    '''
    words = [word for word in word_list if word in model.wv.vocab]
    return np.mean(model.wv.__getitem__(words), axis=0)


def create_sentence_vectors(model, questions):
    '''
    Calculates the average vectors for all questions. The order of the sentences list
    will remain in the returned list of vectors.
    :param model: The trained Word2Vec model
    :param questions: A python list of word lists
    :return: A list of average vectors
    '''
    vectors = []
    for i in range(len(questions)):
        word_list = [word for word in questions[i] if word in model.wv.vocab]
        avg_vector = None
        if len(word_list) > 0:
            avg_vector = avg_word_vector(model, word_list)
        vectors.append((i, avg_vector))
    return vectors

