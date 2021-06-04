import sys

while True:
    print("Type exit for exit.")
    response = input()
    if response == "exit":
        sys.exit()
    print   ("You typed " + response + ".")