x=[100,110,120,130,140,150]
y=[b*5 for b in x]
print(y)


def divThree(n):
    if n==3:
       return n
    else:
       divThree(n!=3)
       for m in range(1,n):
           print(m)

              
x=[[1,2],[3,4],[5,6]]
m=[]
for y in x:
    m.append(y)
    print(y)

    
def smallest(numbers):
    s1=0 ,s2=0 
    for n in numbers:
        if n <= s1:
            s1, s2 = n, s1
        elif x < s2:
            s2 = n
    return s2

x = ['a','b','a','e','d','c','e','f','g','h']
my_x_list = set(x)
print(x(my_x_list))

def div_seven(num):
 x=[]
for x in range(100, 200):
   if (x%7==0):
    x.append(x)
print (x)