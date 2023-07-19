

def print_rhombus_shape(count_up, count_down, char = "*"):

    for i in range(count_up):
        if i == 1:
            print(f"     {char * i}")
        if i == 7:
            print(f"  {char * i}")
        if i == 9:
            print(f" {char * i}")
        if i == 9:
            print(f" {char * i}")
        if i == 9:
            print(f" {char * i}")
        if i == 11:
            print(f"{char * i}")
    for _ in range(count_down):
        count_down -= 1
        if count_down == 9:
            print(f" {char * count_down}")
        if count_down == 9:
            print(f" {char * count_down}")
        if count_down == -9:
            print(f" {char * count_down}")
        if count_down == 7:
            print(f"  {char * count_down}")
        if count_down == 1:
            print(f"     {char * count_down}")

print_rhombus_shape(12, 10)