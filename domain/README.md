# NLP Pipeline cli
We created a bunch of tools keeping the unix philosophy in mind. We want our
commands to be able to be chained using pipes.

## Install requirements
To install all requirements for the cli use:
```bash
pip install -r requirements.txt
```

## Commands
With the cli *nlp_pipeline.py* you can:
- extract.py extract a column of a csv
- grammar.py correct known wrong words (res/grammar.txt) of a txt file
- normalize.py normalizes a document by removing non swiss alphabetic characters
- stopwords.py removes stopwords from a document
- stemm.py stemms all words in a document

### Extract.py
On windows please use git bash or change stdout encoding to utf-8.

This example extracts column number 4 from a csv file seperated by comma.
The output is written into *ionesoft_inquiries.txt*.
```bash
> cat ./ionesoft_tickets.csv | ./extract.py -c 4 -s ',' > ionesoft_inquiries.txt
```

The output is written to *stdout*.
```bash
> cat ./ionesoft_tickets.csv | ./extract.py -c 4 -s ','
```

Column output:
```
ich kann die bilder in übungen nicht bearbeiten. ich habe das beook schonn mit einem zeichnungsprogramm verknüpft und teilweise funktioniert es auch.
lückentexte weg daten verloren gegangen von pp 1.3.3 von rabatt
bitte deaktivieren sie dieses gerät. vielen dank.
```

### Grammar.py
On windows please use git bash or change stdout encoding to utf-8.

This example corrects the *ionesoft_inquiries.txt* file generated by
*extract.py*.

The output is written into *corrected_inquiries.txt*.
```bash
> cat ionesoft_inquiries.txt | ./grammar.py > corrected_inquiries.txt
```

Pipe with *extract.py*. The output is written to *stdout*.
```bash
> cat ./ionesoft_tickets.csv | ./extract.py -c 4 -s ',' | ./grammar.py
```

Corrected output:
```
ich kann die bilder in übungen nicht bearbeiten. ich habe das beook schon mit einem zeichnungsprogramm verknüpft und teilweise funaktioniert es auch.
lückentexte weg daten verloren gegangen von pp 1.3.3 von rabatt
bitte deaaktivieren sie dieses gerät. vielen dank.
```

### Normalize.py
On windows please use git bash or change stdout encoding to utf-8.

This example normalizes the *ionesoft_inquiries.txt* file generated by
*extract.py*. It achieves this by removing all non swiss alphabetic characters
from the document.

The output is written into *normalized_inquiries.txt*.
```bash
> cat ionesoft_inquiries.txt | ./normalize.py > normalized_inquiries.txt
```

The output is written to *stdout*.
```bash
> cat ./ionesoft_inquiries.txt | ./normalize.py
```

Normalized output:
```
ich kann die bilder in übungen nicht bearbeiten ich habe das beook schonn mit einem zeichnungsprogramm verknüpft und teilweise funktioniert es auch
lückentexte weg daten verloren gegangen von pp von rabatt
bitte deaktivieren sie dieses gerät vielen dank
```

### Stopwords.py
On windows please use git bash or change stdout encoding to utf-8.

This example removes stopwords in the *normalized_inquiries.txt* file generated
by *normalize.py*. It uses a stopwordlist that can be defined with
*-s/--stopwords*. The default is *res/custom_ch_stopwords.txt*.

The output is written into *cleaned_inquiries.txt*.
```bash
> cat normalized_inquiries.txt | ./stopwords.py > cleaned_inquiries.txt
```

The output is written to *stdout*.
```bash
> cat ./normalized_inquiries.txt | ./stopwords.py
```

Cleaned output:
```
bilder übungen bearbeiten beook schonn zeichnungsprogramm verknüpft teilweise funktioniert
lückentexte daten verloren gegangen pp rabatt
bitte deaktivieren gerät
```

### Stemm.py
On windows please use git bash or change stdout encoding to utf-8.

This example stemms all words in the *cleaned_inquiries.txt* file generated
by *stopwords.py*. It achieves this using the SnowballStemmer from nltk.

The output is written into *stemmed_inquiries.txt*.
```bash
> cat cleaned_inquiries.txt | ./stemm.py > stemmed_inquiries.txt
```

The output is written to *stdout*.
```bash
> cat ./cleaned_inquiries.txt | ./stemm.py
```

Stemmed output:
```
bild ubung bearbeit beook schonn zeichnungsprogramm verknupft teilweis funktioniert
luckentext dat verlor gegang pp rabatt
bitt deaktivi gerat
```