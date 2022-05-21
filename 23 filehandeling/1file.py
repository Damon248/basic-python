# open function to read the content of files 
file = open ('sample.txt','r') #here, meaning of r is reading 
# file = open ('sample.txt') #by default opening mode is reading 
data = file.read()
# data = file.read(5)  #open 1st five cjaracters of file 
# data = file.readline()   #it'll only read 1st line 
print(data)
file.close()

