
import os
import wikipedia

LANGUAGES = {"it": "Italian", "pl": "Polish", "ru": "Russian", "sk": "Slovak", "pt": "Portuguese",
             "ro": "Romanian", "da": "Danish", "sv": "Swedish", "no": "Norwegian", "en": "English",
             "es": "Spanish", "fr": "French", "cs": "Czech", "de": "German", "fi": "Finnish", "et": "Estonian",
             "lv": "Latvian", "lt": "Lithuanian", "fa": "Persian", "hu": "Hungarian", "he": "Hebrew",
             "el": "Greek", "ar": "Arabic"}
MAX_SIZE_OF_ARTICLES = 100000  # in Kb


def get_size_of_all_articles(language):
    path = language + "/"
    return sum(os.path.getsize(path + f) for f in os.listdir(path + '.'))


for language in LANGUAGES:
    i = 1
    wikipedia.set_lang(language)
    os.makedirs(language)
    while get_size_of_all_articles(language) < MAX_SIZE_OF_ARTICLES:
        try:
            page = wikipedia.page(wikipedia.random())
        except (wikipedia.DisambiguationError, wikipedia.exceptions.PageError):
            continue

        filename = language + "/" + str(i) + "-" + language + ".txt"
        f = open(filename, "w")
        try:
            f.write(page.content.encode('utf-8'))
        except UnicodeEncodeError:
            f.close()
            continue
        
        i += 1


