


print("*** Welcome to the babelfish translator ***")
def print_menu():

    text_to_translate = user_text()
    print("""How do you want to translate the text:
    1. Translate to leet speak
    2. Translate to half a sentence
    3. Translate to Yoda speak""")
    selection = input("Please enter your selection:")
    while True:
        try:
            if selection == "1":
                print(f"Number of occurrences: elite = {text_to_translate.count('elite')}, hacker = {text_to_translate.count('hacker')}")
                translated_word = characters_replacer(word_replacer(text_to_translate))
                print(f"The text has been translated to: {translated_word}")
                print_menu()
            elif selection == "2":
                sentence_length = len(text_to_translate)
                sentence_center = len(text_to_translate) // 2
                half_sentence = text_to_translate[:sentence_center]
                print(f"The sentence is '{sentence_length}' characters long.")
                print(f"The center is located at index '{sentence_center}'")
                print(f"The text has been translated to: {half_sentence}")
                print_menu()
            elif selection == "3":
                print(f"The text has been translated to: {shift_word_position(text_to_translate)}")
                print_menu()
            else:
                selection = input("Please select a valid option (1, 2 or 3):")
                continue
        except ValueError:
            selection = input("Please select a valid option (1, 2 or 3):")
            continue


def user_text():
    text_to_translate = input("Enter the text you want to translate (type 'exit' to quit the application):")
    if text_to_translate.lower() == 'exit':
        exit()
    else:
        pass
    return text_to_translate

def word_replacer(text_to_translate):
    replacements = (('hacker', 'haxor'), ('elite', 'leet'))
    new_string = text_to_translate
    for old, new in replacements:
        new_string = new_string.replace(old, new)
    return new_string

def characters_replacer(text_to_translate):
    replacements = (('a', '4'), ('e', '3'), ('i', '1'), ('o', '0'))
    new_string = text_to_translate
    for old, new in replacements:
        new_string = new_string.replace(old, new)
    return new_string

def shift_word_position(text_to_translate):
    original_word = text_to_translate.split()
    shifted_list_one_letter = original_word[-1:] + original_word[:-1]
    shifted_list_three_letters = original_word[-3:] + original_word[:-3]
    shifted_word_one_letter = ' '.join(shifted_list_one_letter)
    shifted_word_three_letter = ' '.join(shifted_list_three_letters)
    replaced_word_one_letter = characters_replacer(word_replacer(shifted_word_one_letter))
    replaced_word_three_letter = characters_replacer(word_replacer(shifted_word_three_letter))
    return replaced_word_one_letter

#start program
print_menu()

