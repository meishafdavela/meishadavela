pizzas=['pepperoni', 'cheese','margherita']
friend_pizzas=pizzas[:]
pizzas.append('hawaiian')
friend_pizzas.append('chicken')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)