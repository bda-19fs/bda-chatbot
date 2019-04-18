import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    'Click==7.0',
    'nltk==3.4',
    'numpy==1.16.2',
    'pandas==0.24.2',
    'untangle==1.1.1'
]

setuptools.setup(
    name='bda-chatbot',
    version='0.0.2',
    author='Alan Meile, Cyrill Jauner',
    author_email='alan.meile@gmail.com',
    description='Source code for the bda chatbot bachelor thesis fs19',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bda-19fs/bda-chatbot',
    package_dir={'': 'app'},
    packages=setuptools.find_packages(),
    scripts=[
        './app/extract.py',
        './app/grammar.py',
        './app/lemm.py',
        './app/normalize.py',
        './app/stemm.py',
        './app/stopwords.py',
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
