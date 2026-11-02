def show_messages(messages):
    for message in messages:
        print(message)
 
 
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
 
 
messages = ['Hello!', 'How are you?', 'See you tomorrow.']
sent_messages = []
 
send_messages(messages[:], sent_messages)
 
print("\nmessages:", messages)
print("sent_messages:", sent_messages)