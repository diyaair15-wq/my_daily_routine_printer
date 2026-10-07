class bird:
    def __init__(self):
        print("A bird is ready .")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("A penguin is ready.")
    def whoisthis(self):
        print("penguin")
    def run(self):
        print("run faster")
peggy = penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()
