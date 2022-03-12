import pytest

def natural(n):
    return n*(n+1)/2
def test_findsum():
    assert natural(5)==15
    #  false assert natural(5) == 135

def factorial(s):
    return 1 if(s==1 or s==0) else s * factorial(s-1)

def test_fact():
    assert factorial(3)==6
    # assert factorial(3) == 100


ls=[]

def factors(t):
    i=1
    while(i<=t):
        if(t%i==0):
            # print(i)
            ls.append(i)
        i=i+1
    return (ls)
st=[1,2,3,6]
def test_facto():
    assert  factors(6)==st