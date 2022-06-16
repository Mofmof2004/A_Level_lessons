from Pizza_app.Global_info import pizza_menu
from Pizza_app.order_summary import order_summary_main

def pizza_order_main():
    pizza_count = 0
    cont = True
    order = []
    while pizza_count <= 20 and cont is True:
        print("Menu:\n"
              "1: Cheese & Tomato, 7.50,\n "
              "2: BBQ Chicken, 7.90\n"
              "3: Meat Feast, 8.10\n"
              "4: Piri-Piri Chicken, 8.80\n"
              "5: Hawaii, 8.90 \n"
              "6: The Mexican, 9.70\n"
              "7: The Works, 9.90")
        now_order = input("Enter: ")
        if int(now_order) in pizza_menu:
            order.append(int(now_order))
            pizza_count += 1
            print("Are you willing to order another pizza: ")
            ask = input("Enter: ")
            if ask.lower() == "no":
                order_summary_main(order)
                cont = False
        else:
            print("Please enter a valid num: ")

