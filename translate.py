from googletrans import Translator

translator = Translator()

text = input("Enter your text : ")
dest = input("Enter the language you want to translate to : ")

translated = translator.translate(text, dest=dest)

print(translated.text)