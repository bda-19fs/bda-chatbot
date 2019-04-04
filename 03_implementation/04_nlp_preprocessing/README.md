# NLP Pipeline cli
We created a bunch of tools keeping the unix philosophy in mind. We want our
commands to be able to be chained using pipes.

## Install requirements
To install all requirements for the cli use:
```bash
pip install -r requirements.txt
```

## Usage
With the cli *nlp_pipeline.py* you can:
- extract a column of a csv as a list.
- ...

### Extract column as list
On windows please use git bash or change stdout encoding to utf-8.

This example extracts column number 4 from a csv file seperated by comma.
The output is written into extract.txt.
```bash
> cat ./ionesoft_tickets.csv | ./extract.py -c 4 -s ',' > extract.txt
```
