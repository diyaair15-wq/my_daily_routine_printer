from abc import ABC, abstractmethod
class abstract_class(ABC):
    def print(self,x):
        print("passed value:", x)
    @abstractmethod
    def task(self):
        print("we are inside abstract task")
class test_class(abstract_class):
    def task(self):
        print("we are inside test class task")
    test_obj = test_class()
    test_obj.task()
    test_obj.print(100)