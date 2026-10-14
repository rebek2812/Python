answers={}
while True:
    command = input().split()
    if command[0] == "DEPOSIT":
        answers[command[1]]=answers.get(command[1],0)+int(command[2])
    if command[0] == "INCOME":
        for key in answers:
            answers[key]= answers[key] + answers[key]*5/100
    if command[0] == "WITHDRAW":
        answers[command[1]]=answers.get(command[1],0)-int(command[2])
    if command[0] == "BALANCE":
        for key in answers:
            if key == command[1]:
                print(answers[key])
            elif command[1] not in answers:
                print("ERROR")
    if command[0] == "TRANSFER":
            answers[command[1]]=answers.get(command[1],0)-int(command[3])
            answers[command[2]]=answers.get(command[2],0)+int(command[3])
