#Do not trust this code, does not work
print("This program will transform input into pig latin")
Cont = False
while Cont == False:
    beforePig = input("What shalt thou make pig? : ")
    #File = open('piglatin.txt', a)
    print(len(beforePig))
    afterPig = beforePig[0]
    beforePig.append(afterPig)
    break
print(len(afterPig))
print(afterPig)
input("awaiting input...")
