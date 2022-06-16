from Pizza_app.Global_info import costumer_detail
from Pizza_app.Pizza_order import pizza_order_main
def costumer_detail_main():
   number = ""
   Name = input("Please enter your name: ")
   address = input("Pleaase enter your address: ")
   while len(number) != 9:
      number = input("Please enter your telephone number: ")
   costumer_detail[Name] = address, number
   pizza_order_main()



