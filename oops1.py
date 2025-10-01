#initiate a clss
class employee:
    #specil method/mgic_method/ - constructor

    def __init__(self):
        print("started executing attributes/data")
        self.id= 123
        self.salary= 50000
        self.designation = "SDE"
        print("attribute/data have been initiated")

    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

#create an obj/instance of the class
sam=employee()

# print(sam.salary)

#calling a method
# sam.travel("up")

print(type(sam))

