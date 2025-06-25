class student:
    def __init__(self):
        name=input("please enter your name :")
        print("your name is :",name)
        self.name = name
        marks1=int(input("enter marks of subject one : "))
        marks2=int(input("enter marks of subject two : "))
        marks3=int(input("enter marks of subject three : "))
        print("your marks are : ",marks1, marks2, marks3)
        self.marks = [marks1, marks2, marks3]
    def get_avg(self):
        total=0
        for val in self.marks:
            total+=val
            avgs=total/len(self.marks)
        print("Hello",self.name, "your everage marks is :",avgs)
s1=student()
s1.get_avg()      