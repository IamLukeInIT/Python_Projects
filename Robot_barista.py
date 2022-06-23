#Robot barista
print("Hello, welcome to Luke Coffe")
name = input("What is your name?\n")
#we don't serve for evil Ben and Kate
if name == "Ben" or name == "Kate":
    evil_status = input("Are you evil? \n")   
    if evil_status == "Yes":
        print("You're not welcome here " + name + "Get out from here!")    
        exit()
    if evil_status == "No":
        print("Oh, so come on in!")
    
if name != "Ben" or name != "Kate":       
    print("Hello "+ name + ", thank you so much for comming in today.")
    menu = "Black Coffee, Espresso, Latte, Cappucino"
    print(name + ", what would you like from our menu today. Here is what we are serving today:\n" + menu)
    order = input()
    if order in menu:
        if order == "Black Coffe":
            price = 8
        elif order == "Espresso":
            price = 10
        elif order == "Latte":
            price = 12
        elif order == "Cappucino":
            price = 14   
        quantity = input("How many " + order + " you want?\n")
        first_bill = price * int(quantity)

        additional_order = input("Do you want another kind of coffee?\n")
        if additional_order == "Yes":
            add_order = input("What would do you like?\n")
            if add_order == "Black Coffee":
                add_price = 8
            elif add_order == "Espresso":
                add_price = 10
            elif add_order == "Latte":
                add_price = 12
            elif add_order == "Cappucino":
                add_price = 14   
            add_quantity = input("How many " + add_order + " you want?\n")
            second_bill = add_price * int(add_quantity)

            total = first_bill + second_bill
            total_quantity = int(quantity) + int(add_quantity)  
            total_quantity = int(quantity) + int(add_quantity)  

            if int(total_quantity) in range (1, 5):
                print("Thank you. Your total is: $"+ str(total))
                print("We'll have your " + str(quantity) + " " + order + " and " + str(add_quantity) + " "  + add_order + " ready for you in a moment.")
            else:
                print("Thank you. Your total is: $"+ str(total))
                print("We'll have your " + str(quantity) + " " + order + " and " + str(add_quantity) + " " + add_order + " ready for you in a few minutes.")
        else:
            print("Thank you. Your total is: $"+ str(first_bill))
            print("We'll have your " + order + " ready for you in a moment.")            
    else:
        print("I'm so sorry. We don't have " + order + " in our shop.")
