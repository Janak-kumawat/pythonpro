class student:
    def __init__(self, name):
     self.name = name 
s1= student("janak")
a1= student("Ram")
print(s1.name)
print(a1.name)
del s1.name
print(s1.name)