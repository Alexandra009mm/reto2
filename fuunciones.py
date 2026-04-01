Id = 0
def register(dic_clientes):
    global Id 
    keep_register = "yes"
    while keep_register == "yes":
        try:

            name = input("enter your name: ")

            email = input("enter your andress email: ")


            new_costumer = { 
                "name": name, 
                "email": email
                }
            
            Id += 1

            dic_clientes[Id] = new_costumer 
 
         
        except ValueError:
            print("Error")
            continue   
        
        
        print("successful registration! :)")
        print(f"your ID is {Id}")

        

        keep_register = "no"


    return dic_clientes

def add_product(dic_product):
    keep_register = "yes"
    while keep_register == "yes":
        try:
            product_id = int(input("enter product ID: "))

            product_name = input("enter the product name: ").lower()

            price = float(input("enter price: "))

        except ValueError:
            print("error in add product, try again")
            continue

        new_product = (product_name, price)

        dic_product[product_id] = new_product

        keep_register = input("do you want to add other product? yes/no: ") 

        if keep_register != "yes" and keep_register != "no":
            print("Error, The answer must be yes or no.")
            continue

        elif keep_register == "no":
            print("successful product registration! :)")
            keep_register = "no"


        return dic_product
    
def creation_orders(dic_clientes,dic_product,dic_orders):
    keep_register = "yes"
    while keep_register == "yes":
        Id = int(input("enter your ID: "))

    for a in dic_clientes:
        if a["Id"] == Id:
            for i in dic_product:
                print(f"product:{i[0]}, price: {i[1]}")
                order_product = int(input("Enter the product ID you want to order"))

                if order_product == i["product_id"]:
                    quantity = int(input("enter the quantity: "))


            dic_new_orders ={
                "customer":  a["name"],
                "product": i[0],
                "quantity": quantity
                }
            
            dic_orders[a["Id"]] = dic_new_orders

        else:
            print("user not found")
            continue

    
        print("Order successfully placed! :)")

        keep_register = input("do you want to add other order? yes/no: ") 
        if keep_register != "yes" and keep_register != "no":
            print("Error, The answer must be yes or no.")

            return dic_orders

            


        





                

            


        








    

