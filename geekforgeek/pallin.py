def pallindrome(n):
    temp=n
    rev=0
    d=0
    while(n!=0):
        d=n%10
        rev=(rev*10)+d
        n//=10
    return rev
print(pallindrome(371))

#recursive version of the above code
###########_______-------->>>-------------------------------xxxxxx--x-x------------------------x-----------------------x
def rec_pallin(n,dummy):
    if n==0:
        return
    dummy=(dummy*10)+(n%10)
    return rec_pallin(n//10,dummy)

print(rec_pallin(371,0))