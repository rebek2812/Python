answers={}
while True:
    text = input().split()

    if text[0]=="END":
        break

    for word in text:
        answers[word]=answers.get(word,0) + 1
answers=sorted(answers.items())
print(*answers)

