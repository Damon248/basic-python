#  with is like shortcut for reading,writing ... files and we don't need to close() the file all the time 

with open('sample.txt','r') as file:
    a=file.read()

with open('sample.txt','w') as file:
    a=file.write("this is a new sample.txt")
    print(a)