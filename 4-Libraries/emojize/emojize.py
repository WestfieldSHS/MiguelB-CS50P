import emoji

language_type = 'en'
code = input("Input a code for an emoji: ")
if "_" not in code:
    language_type = 'alias'
print(emoji.emojize(code, language=language_type))