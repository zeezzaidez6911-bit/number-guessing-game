import random

num = random.randint(1, 10)  
num=int(num)



attempts=0
guess=None

attempts=attempts+1

while num !=guess:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts=attempts+1
        if num > guess:
            print("too low try again ..")

        elif num < guess:
            print("too High try again..")
    
    except ValueError:
        print("Please enter a valid number")
        
print("you got it right",num,"with ",attempts,"attempts")
    
