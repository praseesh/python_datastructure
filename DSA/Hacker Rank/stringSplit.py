def split_and_join(line):
    a = line.split(" ")
    b = "-".join(a)
    return(b)

line = input()
result = split_and_join(line)
print(result)