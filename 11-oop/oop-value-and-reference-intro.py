#Value
x = 5
name = "udoka"
my_list = [1, 2, 3]


#Reference -> Pointer
list1 = [1, 2, 3]
list2 = list1

tuple1 = (1, 2, 3)
tuple2 = tuple1

print(tuple2)

list2.append(4)
print(list1) #[1,2,3,4]

# list1 and list2 both refers to the same object in memory
# they both hold references to same memory address.