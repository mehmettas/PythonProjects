import random
my_word=[]
def words():
    while True:
        true = []
        false = []
        a=input("Enter the word or -1 for exit : ")
        if a=="-1":
            return random.choice(my_word)
            break
        my_word.append(a)

true=[]
false=[]
a=0
b=0
xx = words()
while True:
    let=input("Guess a letter : ")
    if len(let)!=1:
        print("Enter Just one character")
        continue
    elif not let.isalpha():
        print("Enter a character!")
        continue
    if let in true:
        print("Enter different value")
        continue

    for each in xx:
        if let==each:
            true.append(let)
        else:
            false.append(let)

    for ea in xx:
        if ea in true:
            print(ea,end='')
        else:
            print("_",end='')

    if let in xx:
        a+=1
    else:
        b+=1

    print("")
    print("Life : {} 7".format(b))
    if len(false)==7:
        print("Game Over ! word was {}".format(xx))
        ch=input("Do you want to play again ? y/n")
        if ch=="Y" or ch=="y":
            words()
        else:
            break
    if len(true)==len(xx):
        print("You got it ! word : {}".format(xx))
        ch = input("Do you want to play again ? y/n ")
        if ch == "Y" or ch == "y":
            words()
        else:
            break

