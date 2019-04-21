from bda_core.entities.training.vectorizer import (
    fit_concepts
)


concepts = [
    'Dropbox acquired document collaboration company Hackpad in April 2014. A year later, Dropbox launched a Dropbox Notes note-taking product in beta testing phase. Dropbox Paper was officially announced on October 15, 2015, followed by an open beta and release of mobile Android and iOS apps in August 2016. Dropbox Paper was officially released on January 30, 2017.',
    'Writing for "TechRadar", John Brandon wrote that Dropbox Paper "might be a light tool for now without the extensive templates of Microsoft Office or the integration with other apps in the Zoho suite, but it does work well with the Dropbox storage service that is so popular with office workers these days."',
    'Dropbox Paper, or simply Paper, is a collaborative document-editing service developed by Dropbox. Originating from the companys acquisition of document collaboration company Hackpad in April 2014, Dropbox Paper was officially announced in October 2015, and launched in January 2017. It offers a web application, as well as mobile apps for Android and iOS.'
]

def test_fit_concepts():
    X, vectorizer = fit_concepts(concepts)
    assert X.shape == (3, 93)
    assert vectorizer != None
