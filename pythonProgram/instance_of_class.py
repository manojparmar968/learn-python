"""
Python Program to Get the Class Name of an Instance
"""

class prabhu:
    # def __init__(self,name,age):
    #     self.name = name
    def name(self,name):
        return name

a = prabhu()
print(a.__class__.__name__)
print(type(a).__name__)
    