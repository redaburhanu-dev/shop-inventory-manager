products=[]
# c111: function with multiple prametrs
def calculate_total(price,quantity):
    total = price*quantity
    return total
   #c111+c112  create and save a product
def add_product(name,price ,stock):
   product ={"name" : name , "price" : price, "stock" : stock}
   products.append(product)
   return product 
# c113 dictionarry as afunction parmatr 
def show_product(product):
    print("name:" , product["name"])
    print("price:" , product["price"])
    print("stock:" , product ["stock"])
    print("======")
    #c14+c115 
# return muatiple vaues 
# and call another function
def sell_product (name,quantity):
     for product in products :
         if quantity <=0 or quantity > product[stock]:
             return Fals,0,product["stock"]
             total = calculate_total(product["price"],quantity)
             product["stock"] -=quantity
             return True,total,product["stock"]
         return Flase,0,0
         
             
         

   
