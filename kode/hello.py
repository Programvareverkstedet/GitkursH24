import os 

print("Hello World!")

files = os.listdir("deltakere")
for f in files:
    print("Hello - ", f)

