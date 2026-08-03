def age_counter():
    try:
        a = input("Enter your age: ")
        
        # Check if age is valid
        if a.isalpha() or int(a)<0 :
            print("Error: Age entered is not realistic.")
        else:
            age=int(a)
            print(f"Age entered is {age}.")
            
            # Check if age is even or odd
            if age % 2 == 0:
                print("The age is even.")
            else:
                print("The age is odd.")
                
    except ValueError:
        print("Error: Please enter a valid integer for age.")

# Run the function
age_counter()