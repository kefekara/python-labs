print("WELCOME TO MY QUIZ")

oynamak = input ("do you want to play with me?")
print (oynamak)

if oynamak != "yes":
    quit()

print ("Let's play :)\n")

cevap = input ("What does cpu stand for? \n")

if cevap == "central processing unit":
    print("correct")
else:
    print ("Wrong")

cevap = input ("What does Gpu stand for? \n")
if cevap == "graphics processing unit":
    print("correct")
else:
    print ("Wrong")

cevap = input ("What does RAM stand for? \n")
if cevap == "random access memory":
    print("correct")
else:
    print ("Wrong")