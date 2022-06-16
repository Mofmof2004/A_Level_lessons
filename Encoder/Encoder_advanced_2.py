import random



def decoding():
    encoded_message = input("Enter the message: ")
    message_list = []
    word_list = []
    decoded_message = []
    final_message = []

    number = list(encoded_message)
    for index in range(len(encoded_message)):
        if number[0] == " ":
            message_list.append("".join(word_list))
            number.remove(number[0])
            word_list.clear()
        elif number[0] != " ":
            word_list.append(number[0])
            number.remove(number[0])
    for i in range(len(message_list)):
        decoded_message.append((int(message_list[i]) - int(list(encoded_message)[-1])) / int(list(encoded_message)[-1]))
        final_message.append(chr(int(decoded_message[i])))
    print("".join(final_message))

def encoding():
    messagelist = []

    num = random.randint(2, 9)

    message = input("Enter the message: ")

    for x in range(len(message)):
        messagelist.append(ord(message[x]))

        messagelist[x] = num * int(messagelist[x]) + num

    listToStr = ' '.join([str(elem) for elem in messagelist])
    listToStr += (" " + str(num))

    print(listToStr)
    decoding()


print("Its a linear equation with the form nx+n ")
encoding()
