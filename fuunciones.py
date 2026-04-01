def register(dic_clientes):
    keep_register = "yes"
    while keep_register == "yes":
        try:
            Id = int(input("enter your ID: "))

            name = input("enter your name: ")

            email = input("enter your andress email: ")


            new_costumer = { 
                "name": name, 
                "email": email
                }
            
            dic_clientes[Id] = new_costumer 
        except ValueError:
            print("Error")
            continue

        print("successful registration! :)")
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
        if keep_register not in ["yes", "no"]:
            print("Error, The answer must be yes or no.")
            continue 

        return dic_product
    
def creation_orders(dic_clientes,dic_product):
    keep_register = "yes"
    while keep_register == "yes":
        Id = int(input("enter your ID: "))

    for i in dic_clientes:
        if i["Id"] == Id:
            for i in dic_product:
                print(f"product:{i[0]}, price: {i[1]}")


                

            


        








    

