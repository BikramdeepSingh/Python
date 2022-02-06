msg=input(">")
words= msg.split(' ') #returns a list of string items
emojis = {
    'happy': ":)",
    'sad': ":("
}
output=""

for word in words:
    output +=emojis.get(word, word) + " "

print(output)