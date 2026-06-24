amount=int(input("Enter the thai bath: "))
thai_bath1=amount//100
thai_bath2=(amount%100)//50
thai_bath3=((amount%100)%50)//10
print("notes of 100 bath is:",thai_bath1)
print("notes of 50 bath is:",thai_bath2)
print("notes of 10 bath coins is:",thai_bath3)