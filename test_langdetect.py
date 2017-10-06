
import os

import langdetect as ld

# Lo que quiero hacer es probar contra el lote de train y luego contra uno de test para ver la precision de los
# resultados.
# Luego, puedo hacer un grid search contra el lote de test.


def test_data(profiles, dir_path):
    right = 0
    wrong = 0
    print "Test in %s" % dir_path
    for language in ld.LANGUAGES:
        print "Language:", language

        lang_right = 0
        lang_wrong = 0
        path = dir_path + language + "/"
        for filename in os.listdir(path):
            with open(path + filename, 'r') as f:
                text = f.read()
                f.close()
                profile_text = ld.create_text_profile(text)
                results = ld.detect_language(profiles, profile_text)
                detected_language = results[0][0]

                if detected_language == language: lang_right += 1
                else: lang_wrong += 1

        right += lang_right
        wrong += lang_wrong

        print "Right: %s, Wrong: %s Total: %s" % (str(lang_right), str(lang_wrong), str(lang_right + lang_wrong))
        print "Accuracy: %s " % str(lang_right / float(lang_right + lang_wrong) * 100)

    print "\nTOTAL:"
    print "Right: %s, Wrong: %s Total: %s" % (str(right), str(wrong), str(right + wrong))
    print "Accuracy: %s " % str(right / float(right + wrong) * 100)


def test_accuracy():
    profiles = ld.create_languages_profiles()

    training_data_path = os.getcwd() + ld.PATH_DATASETS
    test_data(profiles, training_data_path)

    testing_data_path = os.getcwd() + ld.PATH_DATASETS + "testing/"
    test_data(profiles, testing_data_path)




test_accuracy()