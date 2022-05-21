# progrram to check if there is a given word available in the text file or not 

file = open ('text1.txt','r')
a=file.read()
if 'cure' in a :
    print ("yes, there is word 'cure' in this text file! ")
else :
    print("there is no word 'cure' in this text file")
file.close()

