txt_messages = ['Hello sweetie', 'ELLO MATE', 'Shrimp on the barbie']
txt_messages_done = []


def show_messages(messageList):
    for message in messageList:
        print(message)


def send_messages(messageList, completedList):
    while messageList:
        current_msg = messageList.pop()
        print(current_msg)
        completedList.append(current_msg)


show_messages(txt_messages)
send_messages(txt_messages, txt_messages_done)

print(txt_messages)
print(txt_messages_done)
