import setuptools

long_description = '''
BDA Chatbot fs19

BDA Chatbot implementation for NLP Pipeline. Currently supports following NLP strategies:
- normalization
- remove stopwords
- stemming
- lemmatization

Example
> echo "Hallo liebe Welt!" | python3 normalize.py | python3 stemm.py

hallo lieb welt
'''

INSTALL_REQUIRES = [
    'Click==7.0',
    'nltk==3.4',
    'numpy==1.16.2',
    'pandas==0.24.2',
    'untangle==1.1.1'
]

setuptools.setup(
    name='bda-chatbot',
    version='1.0.0',
    author='Alan Meile, Cyrill Jauner',
    author_email='alan.meile@gmail.com',
    description='Source code for the bda chatbot bachelor thesis fs19',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bda-19fs/bda-chatbot',
    packages=setuptools.find_packages(),
    include_package_data=True,
    scripts=[
        './extract.py',
        './grammar.py',
        './lemm.py',
        './normalize.py',
        './stemm.py',
        './stopwords.py',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>3.6',
    setup_requires=['setuptools==40.8.0'],
    install_requires=INSTALL_REQUIRES
)
