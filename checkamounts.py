import os, os.path

# simple version for working with CWD

print()
for x in os.listdir("./data"):
    print(x, len(os.listdir("./data/" + x)))
