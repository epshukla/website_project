from common_utility_functions import *

def view_cart(my_cart):
  for product_id in range(len(my_cart)):
    print(colored(str(product_id)+":\t"+str(my_cart[product_id]), 'blue', attrs=['bold']))
  print(colored("Total price: " + str(calculate_total(my_cart)) + '\n', 'red', attrs=['bold']))

def enter_address():
  print(colored("Please enter your address below...", 'green', attrs=['bold']))
  Flat_No =str(input("House/flat no.: "))
  Building=str(input("Building Name: "))
  Loacality=str(input("Locality: "))
  City=str(input("City: "))
  PinCode=int(input("PinCode: "))
  return Flat_No, Building, Loacality, City, PinCode

def enter_payment_option():
  print(colored("Which payment option would you prefer?",'green',attrs=['bold']))
  print("1.Cash on Delivery")
  print("2.Debit/Credit Card")
  Payment_Option=int(input("Choose an option from above: "))
  return Payment_Option

def enter_card_info():
  print(colored("Please enter your card details below...", 'green', attrs=['bold']))
  Card_No=int(input("Enter Card No.: "))
  PIN=int(input("Enter PIN: "))
  return Card_No, PIN


def add_product_to_cart(product_id,quantity,my_cart):
  all_products[product_id][2]-=quantity
  Name = all_products[product_id][0]
  Price = all_products[product_id][1]
  my_cart.append([Name, Price, quantity])


def checkout(my_cart):
  view_cart(my_cart)
  Flat_No, Building, Loacality, City, PinCode=enter_address()
  Payment_Option=enter_payment_option()
  if Payment_Option==2:
    Card_No, PIN=enter_card_info()
    if Card_No in card_info:
      if card_info[Card_No]==PIN:
        print("Payment is succesfull")
        print("Thank You for choosing Eshan's Bakery!")
      else:
        print("invalid PIN")
    else:
      print("Card number is invalid")
  else:
    if Payment_Option==1:
      print("Thank you for choosing Eshan's bakery!!")
      print("Please keep adequate cash handy")
    else:
      if Payment_Option==3:
        print("Exiting program...")
        return "exit"
    return "continue"

def product_menu(my_cart):
  while True:
    print("1.Add more products \n2.Checkout \n3.View cart")
    option_no = int(input("Choose an option: "))
    if option_no==2:
      return
    if option_no==3:
      view_cart(my_cart)


    elif option_no==1:
      view_stock()
      product_id= enter_product_id()
      quantity=int(input("How many would you like? "))
      add_product_to_cart(product_id,quantity,my_cart)

def calculate_total(my_cart):
  total=0
  for product_id in range(len(my_cart)):
    Price= my_cart[product_id][1]
    quantity=my_cart[product_id][2]
    total+=Price*quantity
  return total





