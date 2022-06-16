from Pizza_app.Global_info import *

def order_summary_main(order):
    sum = 0

    print("Name: " + list(costumer_detail)[-1])
    print("Address:  " + str(list(costumer_detail)[-1][0]))
    print("Telephone number: "+ str(list(costumer_detail)[-1][1]))
    print()
    for index in range(len(order)):
        sum += pizza_menu[int(order[index])][1]
    print(sum)
