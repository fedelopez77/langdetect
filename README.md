# langdetect
Language detection library in Python. Implementation based on n-gram text categorization, according to the article [N-Gram-Based Text Categorization](http://odur.let.rug.nl/~vannoord/TextCat/textcat.pdf)

## Usage

Given a text, it returns a list of tuples of length `MAX_RESULTS`, sorted according to the probabilites of that text belonging to each language. The tuples are `(language_code, probability)`. The language codes follow the [ISO 639-1 Standard](https://www.w3schools.com/TAgs/ref_language_codes.asp)

- Library usage:

```python
>>> text = """Automatic summarization is the process of reducing a text document with a
computer program in order to create a summary that retains the most important points
of the original document. As the problem of information overload has grown, and as
the quantity of data has increased, so has interest in automatic summarization.
Technologies that can make a coherent summary take into account variables such as
length, writing style and syntax. An example of the use of summarization technology
is search engines such as Google. Document summarization is another."""

>>> import langdetect as ld
>>> print ld.detect_language(text)
[('en', 0.8657936828582331), ('fr', 0.11200285727639105), ('es', 0.022203459865375846)]
```

Since building the models for every language it is a time consuming operation, to perform many detections it is better to use:

```python
>>> profiles = ld.create_languages_profiles()
>>> ld.detect_language(text, profiles)
```

- Command-line usage:

```    
cd path/to/folder/langdetect/
python langdetect.py -f FILE
``` 

## Datasets
The datasets to train, validate and test the software were collected with [this scrapper](https://github.com/fedelopez77/langdetect/tree/master/datasets/wikiscrapper.py) from Wikipedia articles.

## Available Languages
| Language      | Code          |
| ------------- | ------------- |
| ar | Arabic |
| cs | Czech |
| da | Danish |
| en | English |
| et | Estonian |
| fi | Finnish |
| fr | French |
| de | German |
| el | Greek |
| he | Hebrew |
| hu | Hungarian |
| it | Italian |
| lv | Latvian |
| lt | Lithuanian |
| no | Norwegian |
| fa | Persian |
| pl | Polish |
| pt | Portuguese |
| ro | Romanian |
| ru | Russian |
| sk | Slovak |
| es | Spanish |
| sv | Swedish |
