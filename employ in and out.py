class employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
    def __del__(self):
        print("Destructor called, employee deleted.")
    def create_object():
    print("making object")
    object = employee()
    print("function endded")
    return object
print("calling create_object()function...")
object =create_object()
print("program endded")