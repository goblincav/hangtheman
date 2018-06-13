incorrect_letters = []
sentence = "aah my house"
correct_letters = []
converted_sentence = []
num_of_guess = 5
for z in range(len(sentence)):
    if sentence[z] == " ":
        converted_sentence += " "
    else:
        converted_sentence += "_"
while True:
    final_sentence = ""
    for x in range(len(converted_sentence)):
        final_sentence += converted_sentence[x]
    print(final_sentence)
    if final_sentence == sentence:
        print("WOOOah you'r a very cool person!!")
        break
    guessesleft = num_of_guess - len(incorrect_letters)
    print("You have "+str(guessesleft)+" lives left.")
    num = 0
    inputt = input("¡¡one!! letter you stinky person")
    for y in range(0, len(sentence)):
        if  inputt == sentence[y]:
            correct_letters += inputt
            converted_sentence[y] = inputt
        else:
           num += 1
    if num == len(sentence):
        print("ding dong you're wrong")
        incorrect_letters += inputt
    print("letters you've messed up:",incorrect_letters)
    if len(incorrect_letters) > (num_of_guess-1):
        print("Wah, you're out!")
        break
     

    
        

