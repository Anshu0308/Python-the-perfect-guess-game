from random import randint

number = randint(1, 100)
user_input = -1

count = 1

while user_input != number:
    user_input = int(input("guess the number between 1 and 100 :"))
    if user_input < number :
        print("higher your number please")
        count += 1
    elif user_input > number :
        print("lower your number please")
        count += 1

print("yes , you guess it right !!!")
print(f"number of attempts taken to guess the number {number} is : {count}")