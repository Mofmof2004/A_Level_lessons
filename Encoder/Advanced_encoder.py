import datetime
import random
import operator
sender = 1
signs = ["*", "+", "-", "/"]
coded_key = []
key = []

operator = { "+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.truediv,
}

def key_code(coded_key):
    step_key = []
    lol = []
    for index in range(3):
        key.append(random.choice(signs))
    for index in range(3):
        key.append(random.randrange(2, 9, 1))


    for i in range(6):
        step_key.append(ord(str(key[i])))
        coded_key.append(int(step_key[i])*datetime.datetime.now().hour - datetime.datetime.now().day - sender*5)




    print(coded_key)




def encoding(sender, coded_key):

    key_code(coded_key)
    step_message = []
    coded_message = ""
    message = input("Please enter the message you want to encode: ")
    sender += 1
    for i in range(len(message)):
        remove = ord(message[i])
        coded_key.append(remove)


        for index in range(3):
            op = operator.get(key[index])
            print(key[index])
            print(coded_key[i+6])
            print(key[index + 3])
            print(key)
            coded_key[i+6] = op(int(coded_key[i+6]), int(key[index+3]))



        byte_array = str(coded_key).encode()
        print(byte_array)
        binary_int = int.from_bytes(byte_array, "big")
        coded_message += bin(binary_int)
        # coded_message = str("".join(coded_key))

        # print(step_message)
        print(coded_message)



def decoding():
    coded_message = input("Enter your message: ")
    binary_int = int(coded_message, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()

    print(ascii_text)

encoding(sender, coded_key)
decoding()

