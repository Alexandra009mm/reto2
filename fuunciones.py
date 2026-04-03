from decimal import Decimal

Id = 0
product_id = 0
def register(dic_customers):
    global Id 
    keep_register = "yes"
    while keep_register == "yes":
        try:
#-------------------------------------------------------------------------------------------
#vatidation name
            a = 1
            while a == 1:
                print("-" * 50)
                name = input("enter your name: ").lower().strip()
                if name == "":
                    print("enter a name :/ ") 
                    print("*" * 50)
                    continue
                else:
                     a = 2
#-------------------------------------------------------------------------------------------
# #validation email                  
            b = 2
            while b == 2:
                print("-" * 50)
                email = input("Enter your email address: ").lower().strip()
                
                # Definimos los dominios permitidos
                valid_domains = (".com", "outlook.com", "icloud.com")

                if "@" in email and len(email) > 10 and email.endswith(valid_domains):
                    print("Valid email.")
                    b = 0
                else:
                    print("Error: The email address must contain '@', be longer than 10 characters, and end in .com, outlook.com, or icloud.com")
#------------------------------------------------------------------------------------------------------------
#add data to a new dictionary
            new_customer = { 
                "name": name, 
                "email": email
                }
            
            Id += 1 #assign automatic ID

            dic_customers[Id] = new_customer #That ID is the key to another dictionary
         
        except ValueError:
            print("Error")
            continue   
        

        print("successful registration! :)")
        print("-" * 50)
        print(f"your ID is => {Id}")

        

        keep_register = "no"


    return dic_customers

#----------------------------------------------------------------------------------------------------------


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
    
#----------------------------------------------------------------------------------------------------------

def creation_orders(dic_customers,dic_product,dic_orders):
    keep_register = "yes"
    while keep_register == "yes":

        ask_Id = int(input("enter your ID: "))


        if ask_Id in  dic_customers:
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
                        "customer": dic_customers[ask_Id]["name"] ,
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

#----------------------------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------------------------

def d_calculation(dic_orders):
    total_every_customer = 0
    for orders in dic_orders.values():
         for order in orders:
             total_every_customer += order["subtotal"]

    print(f"The total income for the day is: {total_every_customer}")
    return total_every_customer 

#----------------------------------------------------------------------------------------------------------

def final_generation( dic_orders):
        try:
            ask_Id = int(input("enter your ID: "))

        except ValueError:
            print("error, enter your number ID")
            return

        if ask_Id not in dic_orders:
            print("This customer has no orders.")
            return
        
        total_orders = 0
        t_quantity = 0

       
        print(f"your ID:{ask_Id}")

        for order in dic_orders[ask_Id]:
            print(f"name :  {order['customer']}")
            print(f"Product: {order['product']} | Quantity: {order['quantity']} | Subtotal: {order['subtotal']}")
            t_quantity += order["quantity"]
            total_orders += order["subtotal"]


        orderss = len(dic_orders[ask_Id])
        print(f"Total number of orders placed by the customer: {orderss}" )     
        print("total orders:", total_orders)
        print("total product quantity: ", t_quantity )

        return


#----------------------------------------------------------------------------------------------------------
def final_report(dic_orders): 
    print("FINAL REPORT".center(60, "*"))

    # 1 - Total de pedidos
    total_orders = 0
    for orders in dic_orders.values():
        total_orders += len(orders)
    print("Total orders:", total_orders)
    
    # 2 - Total de ingresos
    total = 0
    for orders in dic_orders.values():
        for order in orders:
            total += order["subtotal"]
    print("Total income: $", total)
    
    # 3 - Pedidos por cliente
    print("Orders by customer:".center(60, "-"))
    for customer_id, orders in dic_orders.items():
        print(f"Customer ID: {customer_id}")
        for order in orders:
            print("Product:", order["product"])
            print("Quantity:", order["quantity"])
            print("Subtotal: $", order["subtotal"])
            print("-" * 20)
    
    # 4 - Productos vendidos
    print("Products sold:".center(60, "-"))
    for orders in dic_orders.values():
        for order in orders:
            print("Product:", order["product"], "| Quantity:", order["quantity"])


def report_menu(dic_orders):
    option = "0"

    while option != "3":
        print("\n" + "=" * 40)
        print(" REPORT MENU ".center(40, "="))
        print("=" * 40)
        print("1. Customer report")
        print("2. General report")
        print("3. Exit")
        
        option = input("Choose an option: ")

        if option == "1":
            final_generation(dic_orders)

        elif option == "2":
            final_report(dic_orders)

        elif option == "3":
            print("Exiting report menu...")

        else:
            print("❌ Invalid option, try again.")