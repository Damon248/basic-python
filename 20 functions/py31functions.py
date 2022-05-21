name =input("ener your name: ")

def greetings (name):
    print("hello there ! welcome, ",name)

greetings(name)

# now let's see default argments 

def greetings (name="stranger"):
    print("hello there ! welcome, ",name)

greetings()   #no values is passed here so, it will print stranger as deault argument
greetings(name)