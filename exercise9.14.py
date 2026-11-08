from random import choice
 
pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')
 
winning_ticket = []
while len(winning_ticket) < 4:
    pull = choice(pool)
    if pull not in winning_ticket:
        winning_ticket.append(pull)
 
print("Any ticket matching these 4 numbers or letters wins a prize:")
print(winning_ticket)