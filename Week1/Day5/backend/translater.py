from Week1.Day5.backend.translater import Translator

def translate ( text, from_language, to_language):
    try :
        instance = Translator (from_language = from_language, to_language = to_language)
        translation = instance.translate(text)
        return translation
    except Exception as e:
        print(e)
        return None
    