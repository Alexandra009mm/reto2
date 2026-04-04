Id = 0

def register(dic_customers):
    global Id 
    print("\n" + "*" * 50)
    print("CUSTOMER REGISTRATION".center(50))
    print("*" * 50)
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
                    print("\nValid email.")
                    b = 0
                else:
                    print("\nError: The email address must contain '@', be longer than 10 characters, and end in .com, outlook.com, or icloud.com")
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
        
        print("\n" + "*" * 50)
        print("successful registration! :)")
        print("-" * 50)
        print(f"your ID is => {Id}")
        print("*" * 50 + "\n")

        keep_register = "no"


    return dic_customers
