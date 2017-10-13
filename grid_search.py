
import os

import langdetect as ld

PATH_VALIDATION = ld.PATH_DATASETS + "validation/"
TESTING_LANGUAGES = {"it": "Italian", "pl": "Polish", "ru": "Russian", "sk": "Slovak", "pt": "Portuguese",
                    "ro": "Romanian", "da": "Danish", "sv": "Swedish", "no": "Norwegian", "en": "English",
                    "es": "Spanish", "fr": "French", "cs": "Czech", "de": "German", "fi": "Finnish", "et": "Estonian",
                    "lv": "Latvian", "lt": "Lithuanian", "fa": "Persian", "hu": "Hungarian", "he": "Hebrew",
                    "el": "Greek", "ar": "Arabic"}


def test_data(profiles, dir_path):
    right = 0
    wrong = 0
    for language in TESTING_LANGUAGES:
        path = dir_path + language + "/"
        for filename in os.listdir(path):
            with open(path + filename, 'r') as f:
                text = f.read()
                f.close()
                try:
                    results = ld.detect_language(text, profiles)
                    detected_language = results[0][0]

                    if detected_language == language:
                        right += 1
                    else:
                        wrong += 1

                except ZeroDivisionError:
                    print "ERROR: " + path + filename


    return right, wrong


def grid_search():
    testing_data_path = os.getcwd() + PATH_VALIDATION

    min_ngrams = [1]
    max_ngrams = [3, 4]
    max_amount_of_ngrams = [350, 400, 450]
    penalization_distances = [700, 800, 900]

    best_precision = 0
    best_min_ngram = best_max_ngram = best_max_amount_of_ngrams = best_penalization_distance = 0

    for min_ngram in min_ngrams:
        for max_ngram in max_ngrams:
            for amount_of_ngrams in max_amount_of_ngrams:
                for penalization_distance in penalization_distances:
                    ld.MIN_NGRAM = min_ngram
                    ld.MAX_NGRAM = max_ngram
                    ld.MAX_AMOUNT_OF_NGRAMS = amount_of_ngrams
                    ld.PENALIZATION_DISTANCE = penalization_distance

                    profiles = ld.create_languages_profiles()
                    right, wrong = test_data(profiles, testing_data_path)
                    precision = right / float(right + wrong)

                    print "min_ngram: %s, max_ngram: %s, amount_of_ngrams: %s, penalization: %s, precision: %s" \
                        % (min_ngram, max_ngram, amount_of_ngrams, penalization_distance, precision)

                    if precision > best_precision:
                        best_precision = precision
                        best_min_ngram = min_ngram
                        best_max_ngram = max_ngram
                        best_max_amount_of_ngrams = amount_of_ngrams
                        best_penalization_distance = penalization_distance

    print "FINAL RESULTS:"
    print "\tBest precision: %s" % best_precision
    print "\tBest min ngram: %s" % best_min_ngram
    print "\tBest max ngram: %s" % best_max_ngram
    print "\tBest amount of ngrams: %s" % best_max_amount_of_ngrams
    print "\tBest penalization: %s" % best_penalization_distance


grid_search()