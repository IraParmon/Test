from translate import Translator


def read_input():
    translator = Translator(to_lang="ru")
    translation = translator.translate(input())
    return translation
