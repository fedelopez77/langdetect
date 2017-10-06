# encoding: cp850

import os
import re
import string
import operator


PATH_DATASETS = '/datasets/'
LANGUAGES = {'en', 'es', 'fr', 'ar', 'cs'}
MIN_NGRAM = 1
MAX_NGRAM = 5
MAX_AMOUNT_OF_NGRAMS = 400
MAX_RESULTS = 3
PENALIZATION_DISTANCE = 500


# Taken from gensim
def to_unicode(text, encoding='utf8', errors='strict'):
    """Convert a string (bytestring in `encoding` or unicode), to unicode."""
    if isinstance(text, unicode):
        return text
    return unicode(text, encoding, errors=errors)


# Taken from gensim
RE_PUNCT = re.compile('([%s])+' % re.escape(string.punctuation), re.UNICODE)
def strip_punctuation(s):
    return RE_PUNCT.sub(" ", s)


# Taken from gensim
RE_NUMERIC = re.compile(r"[0-9]+", re.UNICODE)
def strip_numeric(s):
    return RE_NUMERIC.sub("", s)


def clean_text(text):
    cleaning_functions = [to_unicode, lambda x: x.lower(), strip_punctuation, strip_numeric]
    for f in cleaning_functions:
        text = f(text)
    return text


def add_padding(text):
    # Only one space at the beginning
    padding = " " * (MAX_NGRAM - 1)
    return " " + text + padding


def create_ngrams(text):
    text = add_padding(text)
    for length in range(MIN_NGRAM, MAX_NGRAM + 1):
        for i in range(len(text) - length):
            yield text[i:i + length]


def count_ngrams(ngram_freq, text):
    text = clean_text(text)
    for ngram in create_ngrams(text):
        if ngram in ngram_freq:
            ngram_freq[ngram] += 1
        else:
            ngram_freq[ngram] = 1


def count_ngrams_from_files(language):
    """
    :param language
    :return: dictionary of {ngrams: freq} of all the corpus of the given language
    """
    path = os.getcwd() + PATH_DATASETS + language + "/"
    ngram_freq = {}
    for filename in os.listdir(path):
        with open(path + filename, 'r') as f:
            text = f.read()
            count_ngrams(ngram_freq, text)
        f.close()
    return ngram_freq


def sort_ngrams_by_frequency(ngram_freq):
    """
    :param ngram_freq:
    :return: sorted list of (ngram, freq) in descending order
    """
    return sorted(ngram_freq.items(), key=operator.itemgetter(1), cmp=lambda x,y: cmp(y,x))


def create_profile_dict(sorted_ngrams):
    """
    :param sorted_ngrams: sorted list of (ngram, freq) in descending order
    :return: dictionary of {ngram: (freq, order)}
    """
    profile = {}
    for i in xrange(MAX_AMOUNT_OF_NGRAMS):
        ngram, freq = sorted_ngrams[i]
        profile[ngram] = freq, i
    return profile


def create_profile(ngram_freq):
    sorted_ngrams = sort_ngrams_by_frequency(ngram_freq)
    return create_profile_dict(sorted_ngrams)


def create_language_profile(language):
    ngram_freq = count_ngrams_from_files(language)
    return create_profile(ngram_freq)


def create_languages_profiles():
    return {language: create_language_profile(language) for language in LANGUAGES}


def create_text_profile(text):
    ngram_freq = {}
    count_ngrams(ngram_freq, text)
    return create_profile(ngram_freq)


def measure_profile_distance(profile_text, profile_language):
    result = 0
    for ngram in profile_text:
        if ngram in profile_language:
            position_in_text = profile_text[ngram][1]
            position_in_language = profile_language[ngram][1]
            result += abs(position_in_language - position_in_text)
        else:
            result += PENALIZATION_DISTANCE
    return result


def measure_all_distances(profiles, profile_text):
    result = []
    for language in profiles:
        distance = measure_profile_distance(profile_text, profiles[language])
        result.append((language, distance))
    return result


def process_results(result):
    """
    :param result: list of (language, distance)
    :return: sorted list of length MAX_RESULTS of language and the probability of that language being the right match
    """
    sorted_result = sorted(result, cmp=lambda x,y: cmp(x[1], y[1]))[0:MAX_RESULTS]

    inverted_scores = [1 / float(elem[1]) for elem in sorted_result]
    total = sum(inverted_scores)
    return zip([x[0] for x in sorted_result],[y / total for y in inverted_scores])


def detect_language(profiles, profile_text):
    results = measure_all_distances(profiles, profile_text)
    return process_results(results)


def main(text):
    #text = get_text()   # Conseguir el texto de alguna forma
    profiles = create_languages_profiles()
    profile_text = create_text_profile(text)

    return detect_language(profiles, profile_text)
