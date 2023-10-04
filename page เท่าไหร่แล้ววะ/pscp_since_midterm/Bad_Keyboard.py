"""Bad Keyboard"""
def main(word):
    """swap i-o"""
    data = ""
    for i in word:
        if i == "i":
            i = "o"
        elif i == "o":
            i = "i"
        elif i == "I":
            i = "O"
        elif i == "O":
            i = "I"
        data += i
    print(data)
main(input())
