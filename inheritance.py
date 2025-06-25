class car:
    color="The colour of our cars is red"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped")
class toyotacar(car):
    def __init__(self, name):
     self.name= name  

car1= toyotacar("fortuner") 
car2= toyotacar("prius") 

print(car1.color)
car1.start()
print(car1.name)
print(car2.name)
car1.stop()

        