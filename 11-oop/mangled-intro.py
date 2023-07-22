class Animal:
    __name = ""
    __age = 0

    def __init__(self, name="pan", age="2"):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Negative age value not allowed.")

    def get_age(self):
        return self.__age

my_cat = Animal()
my_cat.set_age(3)
print(my_cat.get_age())


#print(my_cat.__age) # cant access the mangled variable inside the animal class this way

#To access mangled variable we use "my_cat.Animal__age"
print(my_cat._Animal__age)

