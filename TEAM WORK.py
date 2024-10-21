while True:
    print("Please choose your option from the list below:")
    print("1. Learn Python")
    print("2. Learn Java")
    print("3. Go swimming")
    print("4. Have dinner")
    print("5. Go to bed")
    print("0. Exit")

    choice = input("Enter your choice (0-5): ")

    if choice == '1':        
        print("You chose to learn Python.")
    elif choice == '2':
        print("You chose to learn Java.")
    elif choice == '3':
        print("You chose to go swimming.")
    elif choice == '4':
        print("You chose to have dinner.")
    elif choice == '5':
        print("You chose to go to bed.")
    elif choice == '0':
        print("Exiting the program.") 
        break  # Exit the loop
    else:
        print("Wrong choice, Please try again.")
