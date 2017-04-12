#Assigment
#evenly added fabonacci series

a=1
b=1
k=0
num=[1,1]

while k <= 20:
        k = a + b
        a = b
        b = k
        if(k % 2==0):
         num.append(k)
print("Sum of Evenly Fabonacci series:\n"+str(sum(num))) 


