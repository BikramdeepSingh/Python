def emoji_converter(words):
    words= msg.split(' ') #returns a list of string items
    emojis = {
        'happy': ":)",
        'sad': ":("
    }
    output=""

    for word in words:
        output +=emojis.get(word, word) + " "

    return output


msg=input(">")
print(emoji_converter(msg))