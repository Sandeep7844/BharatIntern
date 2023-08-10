from translate import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(to_lang=target_lang, from_lang=source_lang)
    translated = translator.translate(text)
    return translated

source_text = "Hello, how are you?"
source_lang = 'en'  # English
target_lang = 'fr'  # French

translated_text = translate_text(source_text, source_lang, target_lang)
print(f"Source: {source_text}")
print(f"Translated ({target_lang}): {translated_text}")
