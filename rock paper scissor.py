import random
user_choose= int(input("what do you choose?type 0 for rock,1 for paper,2 fro scissor"))
computer_choose = random.randint(0,1)
print(f"computer choose {computer_choose}")

if user_choose==0 and computer_choose==2:
    print("you win!")
elif computer_choose>user_choose:
    print("you lose!")
elif computer_choose==1 and user_choose==2:
    print("you win")
elif computer_choose==0 and user_choose==1:
    print("you win")
elif computer_choose==0 and user_choose==2:
    print("you lose!")
elif computer_choose==user_choose:
    print("draw!")
else:
    print("invalid number")