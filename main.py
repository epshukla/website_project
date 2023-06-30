from seller_utility_functions import *
from customer_utility_functions import *

def customer_process():Customer
  my_cart=[]
  print("Showing stock now...")
  print(colored("Hello Customer!\nShowing the product menu now... What do you want to do next?", 'green', attrs=['bold']))
  product_menu(my_cart)
  action = checkout(my_cart)
  return action


def seller_process():
    Password = enter_password()
    if Password == 4321:
        print("Hello! You have logged in as the seller \nWhat would you like to do? ")
    else:
        return "continue"
    while True:
        print("1.Add products \n2.Remove items \n3.View Stock \n4.Exit")
        option = int(input("Choose an option from above: "))
        if option == 1:
            add_product_to_stock()
        if option == 2:
            remove_product_from_stock()
        if option == 3:
            view_stock()
        if option == 4:
            return "exit"


if __name__ == '__main__':
    while True:
        print("_"*70)
        print(colored("Are you a customer or a seller?", 'green', attrs=['bold']))
        user_type = str(input("Please chose and option from above: "))
        if user_type == "Customer" or user_type == "1":
            action = customer_process()
            if action == "exit":
                break
        if user_type == "Seller" or user_type == "2":
            action = seller_process()
            if action == "exit":
                break
