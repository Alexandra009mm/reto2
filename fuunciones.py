from decimal import Decimal

Id = 0
product_id = 0
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
    global product_id
    keep_register = "yes"
    while keep_register == "yes":
        try:

            product_name = input("enter the product name: ").lower()

            price = Decimal(input("enter price: "))

        except ValueError:
            print("error in add product, try again")
            continue

        new_product = (product_name, price)
        product_id += 1

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

        ask_Id = int(input("enter your ID: "))


        if ask_Id in  dic_clientes:
            for key_product, value in dic_product.items():
                print(f"product ID: {key_product}| producto: {value[0]} | price: {value[1]}")


            order_product = int(input("Enter the product ID you want to order: "))
    
            if order_product in dic_product:
                quantity = int(input("enter the quantity: "))

                subtotal = dic_product[order_product][1] * quantity

            else:
                print("product ID no found")
                keep_register = "no"
                break

            a = "yes"
            while a == "yes":

                confirmation = input("Are you sure you want to place this order? yes/no: ")
                if confirmation == "yes":
                
                    dic_new_orders ={
                        "customer": dic_clientes[ask_Id]["name"] ,
                        "product": dic_product[order_product][0],
                        "quantity": quantity,
                        "subtotal": subtotal
                        }
                    
                    if ask_Id not in dic_orders:
                        dic_orders[ask_Id] = ()

                    dic_orders[ask_Id] = dic_orders[ask_Id] + (dic_new_orders,)
                    print("Order successfully placed! :)")

                    a = 1
                    while a == 1:

                        keep_register = input("do you want to add other order? yes/no: ")

                        if keep_register != "yes" and keep_register != "no":
                            print("Error, The answer must be yes or no.")

                        else:
                            break

                elif confirmation =="no":
                    print("OK, order cancelled")
                    keep_register = "no"
                    break
                
                else:
                    print("Error, The answer must be yes or no.")
                    continue


        else:
            print("user not found")
            continue

    return dic_orders

def order_consultation(dic_orders):
    keep_register = "yes"
    while keep_register == "yes":
        try:
            ask_Id = int(input("enter your ID: "))

        except ValueError:
            print("error, enter your number ID")
            continue


        if ask_Id not in dic_orders:
            print("The customer has not placed any orders.")
            keep_register = "no"

        else: 
            my_order = dic_orders[ask_Id]

            print(f"--- ORDER DETAILS (ID: {ask_Id}) ---")

            for i in my_order:
                for k, v in i.items():
                    print(f"{k}: {v}")
                print("---")      
                
            keep_register = "no"
    return



    
