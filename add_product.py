from decimal import Decimal,InvalidOperation 
product_id = 0
def add_product(dic_product):
    global product_id
    keep_register = "yes"
    while keep_register == "yes":
        try:
            a = 1
            while a == 1:
                print("-" * 50)
                product_name = input("enter the product name: ").lower().strip()
                if product_name == "":
                    print("try again enter a product name :/ ") 
                    print("*" * 50 + "\n")
                    continue
                else:
                    a = 2
            
            b = 1 
            while b == 1:
                try:
                    print("-" * 50)
                    # Convertimos la entrada a Decimal
                    price = Decimal(input("enter price: "))

                    if price <= 0:
                        print("price invalid :/") 
                        print("*" * 50 + "\n")
                        continue
                    else: 
                        b = 2
                        
                except InvalidOperation: # Esto atrapa si escriben letras o símbolos
                    print("enter a valid number")
                    print("*" * 50 + "\n")
                    continue

        except ValueError:
            print("error in add product, try again")
            print("*" * 50 + "\n")
            continue

        product_id +=1

        new_product = (product_name, price)
        

        dic_product[product_id] = new_product

        c = 1
        while c == 1: 
            keep_register = input("do you want to add other product? yes/no: ").lower().strip()

            if keep_register == "no":
                print("successful product registration! :)\n")
                c = 2
                break   # Sale del bucle de la pregunta y keep_register es "no" (termina todo)
            elif keep_register == "yes":
                c = 2  # Sale del bucle de la pregunta y vuelve arriba a registrar otro
            else:
                print("Error, The answer must be yes or no.")
                print("*" * 50 + "\n")

    return dic_product   