class employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
    def __del__(self):
        print("Destructor called, employee deleted.")
def create_obj():
    print("making object")
    obj = employee() 
    print("function endded")
    return obj
print("calling create object function...")
obj =create_obj()
print("program endded")