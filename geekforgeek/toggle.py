def set_bits(n):

    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;

    return (n >> 1) ^ 1
 
def toggle(n):
 
  
    if (n == 1):
        return 1
 
    
    return n ^ set_bits(n)


lst = []
  
# number of elements as input
n = int(input())
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele)

for i in lst:
    print(toggle(i))