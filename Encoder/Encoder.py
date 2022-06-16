import enchant
language = enchant.Dict("en_US")
new_word = 0
which = input("Do you want to encode or decode\n 1 or 2: ")
message = input("Code: ")
encoded_message = ""

if which == "1":
    key = int(input("key: "))
    for index in range(len(message)):
        if message[index] == " ":
            encoded_message += " "
        else:
            letter = ord(message[index]) + key
            encoded_message += (chr(letter))

    print(encoded_message)
elif which == "2":
    for index in range(26):
        encoded_message = ""
        for i in range(len(message)):
            if message[i] == " ":
                encoded_message += " "
                if new_word == 0:
                    new_word = i
            else:
                letter = (ord(message[i]) - index)
                encoded_message += (chr(letter))


        if language.check(encoded_message[: new_word]) is True:
            print(encoded_message)

