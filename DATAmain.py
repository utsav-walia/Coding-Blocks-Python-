
# Open and read file
file = open("hello.txt", "r")
print(file.read(5))
file.close()

# Writing file
file = open("something.txt", "w")
file.write("Hi, my name is abc")
file.close()

# Read from file
file = open("hello.txt", "r")
print(file.readlines())   # Creates a list of all lines
file.close()

# With block
with open("hello.txt", "r") as file:
    print(file.read())
    file.seek(6)
    print(file.read())