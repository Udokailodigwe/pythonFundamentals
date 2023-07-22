#reading into from a file
with open("data/example.txt") as f:   #f is a file object
    for i, line in enumerate(f):
        if i == 0:
            continue
        clean_file = line.rstrip()
        print(clean_file)


#writing into a file
with open("data/sample.txt", "w+") as f:
    for i in range(10):
        f.write(f"This is line number{i}\n")

