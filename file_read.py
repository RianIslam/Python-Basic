with open("file.txt",mode="r") as s_file:
    for line in s_file.readlines():
        print(line,end="")