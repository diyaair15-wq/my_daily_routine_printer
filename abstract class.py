# import necessary modules
from abc import ABC, abstractmethod
# create base class
class abstract_class(ABC):
   # funtion to print passed value
    def print(self,x):
        print("passed value:", x)
#abstract method
    @abstractmethod
    def task(self):
        print("we are inside abstract task")
#create subclass
class test_class(abstract_class):
    def task(self):
        print("we are inside test class task")
  #object of test_class createed
test_obj = test_class()
test_obj.task()
test_obj.print(100)