from termcolor import colored

card_info={12341234:1234}

all_products=[
              ["Black Forest Cake", 450, 3],
              ["Moango Cake", 420, 2]
              ]

seller_password = 4321

def view_stock():
  for product_id in range(len(all_products)):
    print(colored(str(product_id)+":\t"+str(all_products[product_id]), 'green', attrs=["bold"]))


def enter_password():
  Password=int(input("Enter Password: "))
  return Password

def enter_product_id():
  product_id=int(input("Enter the product number from above: "))
  return product_id

