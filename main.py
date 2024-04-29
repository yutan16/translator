from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('./translation.txt', mode='r+') as my_translation:
        translation = translator.translate(my_translation.read())
        print(translation)
        with open('./translated.txt', mode='w') as my_translated:
            my_translated.write(translation)
except FileNotFoundError as err:
    print(f'Error Description: {err}')
