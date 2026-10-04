# File Handling Practice
# Demonstrates how to append text to a file.

file = open("log.txt", "a")
file.write("\nI am testing how append mode works.")
file.close()

# File modes:
# r = read
# w = write
# a = append

# Using the 'with' keyword automatically closes the file
# and helps manage system resources safely.

with open("log.txt", "a") as file:
    file.write("Hello World!")
