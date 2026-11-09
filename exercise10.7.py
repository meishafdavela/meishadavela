print("Enter 'q' at any time to quit.")
 
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
 
    second_number = input("Second number: ")
    if second_number == 'q':
        break
 
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, I can only add numbers. Please enter numbers, not text.")
    else:
        print(f"The sum is {answer}.")