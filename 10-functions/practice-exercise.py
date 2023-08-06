
#def print_rhombus_shape(count_up, count_down, char = "*"):

    #for i in range(count_up):
     #   if i == 1:
      #      print(f"     {char * i}")
       # if i == 7:
        #    print(f"  {char * i}")
        #if i == 9:
         #   print(f" {char * i}")
        #if i == 9:
         #   print(f" {char * i}")
        #if i == 9:
         #   print(f" {char * i}")
        #if i == 11:
         #   print(f"{char * i}")
    #for _ in range(count_down):
        #count_down -= 1
        #if count_down == 9:
         #   print(f" {char * count_down}")
        #if count_down == 9:
         #   print(f" {char * count_down}")
        #if count_down == -9:
         #   print(f" {char * count_down}")
        #if count_down == 7:
         #   print(f"  {char * count_down}")
        #if count_down == 1:
         #   print(f"     {char * count_down}")

#print_rhombus_shape(12, 10)

#Print out circle
def print_circle(radius, char="#"):
    for y in range(-radius, radius + 1):
        #print(f'y is {y}')
        for x in range(-radius, radius + 1):
            #print(f'x is {x}')
            if x ** 2 + y ** 2 <= radius ** 2:
                print(char, end="")
            else:
                print(" ", end="")
        print()

print_circle(5, "*")