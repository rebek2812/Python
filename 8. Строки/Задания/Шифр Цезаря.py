def CaesaCipher(S, k):
    new_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for elem in S:
        if elem.lower() not in alphabet:
            new_str += elem
        else:
            c = alphabet[(alphabet.index(elem.lower()) + k)%len(alphabet)]
            new_str += c if elem.islower() else c.upper()
    return new_str
words = input()

print(CaesaCipher(words, 3))
