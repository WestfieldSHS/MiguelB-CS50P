def indoor_voice(text):
    indoor_voice = text.lower()
    return indoor_voice


if __name__ == "__main__":
    print(indoor_voice("Hello."))
    print(indoor_voice("my name is..."))
    print(indoor_voice("MIGUEL!"))
    print(indoor_voice("what is    your name? "))
