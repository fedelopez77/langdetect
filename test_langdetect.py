
import os

import langdetect as ld

TESTING_LANGUAGES = {"it": "Italian", "pl": "Polish", "ru": "Russian", "sk": "Slovak", "pt": "Portuguese",
                    "ro": "Romanian", "da": "Danish", "sv": "Swedish", "no": "Norwegian", "en": "English",
                    "es": "Spanish", "fr": "French", "cs": "Czech", "de": "German", "fi": "Finnish", "et": "Estonian",
                    "lv": "Latvian", "lt": "Lithuanian", "fa": "Persian", "hu": "Hungarian", "he": "Hebrew",
                    "el": "Greek", "ar": "Arabic"}


def test_data(profiles, dir_path):
    right = 0
    wrong = 0
    print "Test in %s" % dir_path
    print "Language, total, precision"
    for language in TESTING_LANGUAGES:
        # print "Language:", language

        lang_right = 0
        lang_wrong = 0
        path = dir_path + language + "/"
        for filename in os.listdir(path):
            with open(path + filename, 'r') as f:
                text = f.read()
                f.close()
                results = ld.detect_language(text, profiles)
                detected_language = results[0][0]

                if detected_language == language: lang_right += 1
                else: lang_wrong += 1

        right += lang_right
        wrong += lang_wrong

        # print "Right: %s, Wrong: %s Total: %s" % (str(lang_right), str(lang_wrong), str(lang_right + lang_wrong))
        # print "Accuracy: %s " % str(lang_right / float(lang_right + lang_wrong) * 100)
        print "%s, %s, %.2f" % (TESTING_LANGUAGES[language], str(lang_right + lang_wrong), lang_right / float(lang_right + lang_wrong) * 100)


    print "======TOTAL:"
    print "\tRight: %s, Wrong: %s Total: %s" % (str(right), str(wrong), str(right + wrong))
    print "\tAccuracy: %s \n" % str(right / float(right + wrong) * 100)


def test_accuracy():
    profiles = ld.create_languages_profiles()

    # training_data_path = os.getcwd() + ld.PATH_DATASETS
    # test_data(profiles, training_data_path)

    testing_data_path = os.getcwd() + ld.PATH_DATASETS + "testing/"
    test_data(profiles, testing_data_path)


test_accuracy()