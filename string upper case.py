class IOString:
    def __init__(self, default_val: str = "Default String"):
        self.str1: str = default_val

    def get_String(self) -> None:
        self.str1 = input("Enter a string: ")

    def print_String(self) -> str:
        upper_str = self.str1.upper()
        print(f"Uppercase string: {upper_str}")
        return upper_str

str_handler = IOString("Initial Value")
str_handler.get_String()
str_handler.print_String()
