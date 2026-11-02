def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
 
 
make_sandwich('turkey')
make_sandwich('ham', 'cheese')
make_sandwich('tuna', 'lettuce', 'tomato', 'mayonnaise')