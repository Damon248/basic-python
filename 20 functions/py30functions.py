# before using functions 
# marks1=[86,93,88]
# percentage1 = ((marks1[0]+marks1[1]+marks1[2])/300)*100
# marks2=[80,95,82]
# percentage2 = ((marks2[0]+marks2[1]+marks2[2])/300)*100
# print(percentage1)
# print(percentage2)

# after using functions 

def percentage (marks):
    p= ((marks[0]+marks[1]+marks[2])/300)*100
    return p

marks1=[86,93,88]
marks2=[80,95,82]
percentage1= percentage(marks1)
percentage2=percentage(marks2)
print(percentage1,percentage2)


