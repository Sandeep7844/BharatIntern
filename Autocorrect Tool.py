from autocorrect import Speller

def correct_word(input_word):
    spell = Speller()
    corrected_word = spell(input_word)
    return corrected_word

input_word = "gret"
corrected_word = correct_word(input_word)

print(f"Input word: {input_word}")
print(f"Corrected word: {corrected_word}")
