# langdetect
Language detection library in Python. Implementation based on n-gram text categorization, according to the article [N-Gram-Based Text Categorization](http://odur.let.rug.nl/~vannoord/TextCat/textcat.pdf).

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
[('en', 0.9201609943007083), ('fr', 0.07217134307468472), ('ro', 0.0076676626246070185)]
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

## Tests
Just by cloning the test can be run by:

```python
python test_langdetect.py
```

This will print out the resulting detection precision for the train and test dataset, for every language. It could be useful to see the results in case of changing the train dataset or at adjusting parameters of the algorithm.

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


## Adding a new language
1. Add the dataset of the new language inside the `datasets` directory. The dataset should be text files of the given language inside a directory with the language code as name. According to the article, with 100 Kilobytes is enough.
2. Add the language code and name to the `LANGUAGES` dictionary in the `langdetect.py` file.
3. OPTIONAL: if you want to test the new language, add a test dataset under the `datasets/testing` directory. Then, add the language code to the `TESTING_LANGUAGES` dictionary in the `test_langdetect.py` file.