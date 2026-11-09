first_number = input("First number: ")
second_number = input("Second number: ")
 
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Sorry, I can only add numbers. Please enter numbers, not text.")
else:
    print(f"The sum is {answer}.")