# simple spam detector 
a=input("enter a text: ")

if("make money" in a):
    spam=True
elif("subscribe to" in a):
    spam=True
elif("earn now" in a):
    spam=True
elif("get bitcoins" in a):
    spam=True
else:
    spam=False
if(spam):
    print("this is a spam")
else:
    print("this is genuine")

