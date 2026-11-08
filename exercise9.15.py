from random import choice
 
pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')
 
 
def draw_ticket():
    ticket = []
    while len(ticket) < 4:
        pull = choice(pool)
        if pull not in ticket:
            ticket.append(pull)
    return ticket
 
 
my_ticket = [3, 7, 'a', 'e']
 
tries = 0
while True:
    tries += 1
    winning_ticket = draw_ticket()
    if set(winning_ticket) == set(my_ticket):
        break
 
print(f"My ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {tries} tries to win.")