from common_utility_functions import *

def enter_product_info():
  Name=str(input("Enter Name: "))
  Price=str(input("Enter Price: "))
  Stock=str(input("Enter Stock: "))
  return Name, Price, Stock


def add_product_to_stock():
  Name, Price, Stock = enter_product_info()
  all_products.append([Name, Price, Stock])

def remove_product_from_stock():
  product_id=enter_product_id()
  all_products.pop(product_id)
