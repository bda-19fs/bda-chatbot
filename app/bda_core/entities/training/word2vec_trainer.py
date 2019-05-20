import gensim
import numpy as np


class Config:
    '''
    This class represents the configuration for the Word2Vec model.
    '''
    def __init__(self, dimension=150, hierarchical_softmax=0, negative_sampling=0, ns_exponent=0,
                 sample=0, window_size=5, workers=3, use_skip_gram=1, min_count=2, epochs=10):
        self.dimension = dimension
        self.hierarchical_softmax = hierarchical_softmax
        self.negative_sampling = negative_sampling
        self.ns_exponent = ns_exponent
        self.sample = sample
        self.window_size = window_size
        self.workers = workers
        self.use_skip_gram = use_skip_gram
        self.min_count = min_count
        self.epochs = epochs


def fit_model(sentences, config):
    '''
    Fits the Word2Vec model with the given sentences. The vectors were normalized after the training.
    A further training of the model is not possible.
    :param sentences: A python list of sentences
    :param config: The config for the model
    :return: The trained Word2Vec model
    '''
    model = gensim.models.Word2Vec(size=config.dimension, hs=config.hierarchical_softmax, window=config.window_size,
                                   workers=config.workers, sg=config.use_skip_gram, min_count=2)

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


def transpose_vector(vec):
    '''
    Returns a new vector that is the transposition of the given vector.
    :param vec: The vector to transpose
    :return: The transposition vector
    '''
    return vec[np.newaxis]


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
        vectors.append(avg_vector)
    vectors = np.array(vectors)
    return vectors


def create_matrix_from_vectors(vectors):
    '''
    Creates a matrix that contains all vectors of the given vector list as row vectors.
    :param vectors: A list of vectors with the same dimension
    :return: The concatenation matrix of the given vectors
    '''
    vectors_len = len(vectors)
    if vectors_len > 0:
        matrix = transpose_vector(vectors[0])
        for i in range(1, vectors_len):
            vec = vectors[i]
            if vec is not None:
                transposed = transpose_vector(vectors[i])
                matrix = np.concatenate((matrix, transposed), axis=0)
        return matrix
    else:
        raise Exception('the given list of vectors is empty')
