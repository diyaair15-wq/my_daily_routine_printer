medical_cause = input("do you have a medical cause? (yes/no): ").strip().lower()
if medical_cause == "yes":
    print("You are allowed.")
else:
    attendance = int(input("Enter student attendance percentage: "))
    if attendance >= 75:
        print("You are allowed.")
    else:
        print("You are not allowed.")
        