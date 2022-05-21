# replacing specific word from the text file 

with open ("text1.txt","r") as f:
    content = f.read()

content = content.replace("fucking","f*****g")

with open ("text1.txt","w") as f:
    f.write(content)